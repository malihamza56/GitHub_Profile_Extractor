
import streamlit as st
from main import extract_profile
import os
import json

import subprocess
import sys

def ensure_chromium():
    try:
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        st.error(f"Chromium install failed: {e}")

ensure_chromium()


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="GitHub Profile Extractor",
    page_icon="🐙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS — PREMIUM THEME
# ==========================================

st.markdown("""
<style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    /* Main background */
    .stApp {
        background:
            radial-gradient(circle at 8% 8%, rgba(99, 102, 241, 0.16), transparent 40%),
            radial-gradient(circle at 92% 15%, rgba(56, 189, 248, 0.12), transparent 40%),
            radial-gradient(circle at 50% 100%, rgba(168, 85, 247, 0.08), transparent 45%),
            #05060a;
        color: #f3f5f9;
    }

    /* Hide default streamlit chrome */
    #MainMenu, footer, header {visibility: hidden;}

    /* Main container */
    .block-container {
        max-width: 1120px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* ============== HERO ============== */
    .hero {
        text-align: center;
        padding: 40px 20px 30px;
        animation: fadeIn 0.6s ease;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(99, 102, 241, 0.12);
        border: 1px solid rgba(99, 102, 241, 0.35);
        color: #a5b4fc;
        font-size: 12.5px;
        font-weight: 600;
        letter-spacing: 0.03em;
        padding: 6px 14px;
        border-radius: 999px;
        margin-bottom: 22px;
        text-transform: uppercase;
    }

    .hero-icon {
        font-size: 52px;
        margin-bottom: 6px;
        filter: drop-shadow(0 8px 24px rgba(99, 102, 241, 0.35));
    }

    .hero h1 {
        font-size: 48px;
        font-weight: 900;
        margin: 6px 0 14px;
        letter-spacing: -1.4px;
        background: linear-gradient(135deg, #ffffff 30%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        color: #97a1b3;
        font-size: 16.5px;
        max-width: 620px;
        margin: auto;
        line-height: 1.7;
        font-weight: 400;
    }

    /* ============== INPUT ROW ============== */
    .input-wrap {
        max-width: 640px;
        margin: 34px auto 0;
    }

    .stTextInput input {
        background: rgba(255,255,255,0.045) !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        color: white !important;
        border-radius: 14px !important;
        padding: 15px 18px !important;
        font-size: 15px !important;
        transition: all 0.25s ease;
    }

    .stTextInput input:focus {
        border-color: rgba(99, 102, 241, 0.6) !important;
        box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.14) !important;
    }

    .stTextInput input::placeholder {
        color: #5b6376 !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 14px;
        border: none;
        background: linear-gradient(135deg, #6366f1, #3b82f6 60%, #38bdf8);
        background-size: 160% 160%;
        color: white;
        font-weight: 700;
        font-size: 15px;
        letter-spacing: 0.01em;
        transition: 0.3s ease;
        box-shadow: 0 8px 24px rgba(59,130,246,0.22);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        background-position: 100% 0%;
        box-shadow: 0 14px 34px rgba(99,102,241,0.38);
    }

    .stButton > button:active {
        transform: translateY(0px);
    }

    /* ============== CARDS ============== */
    .card {
        background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 26px 28px;
        margin-top: 22px;
        backdrop-filter: blur(16px);
        animation: fadeIn 0.5s ease;
        box-shadow: 0 4px 24px rgba(0,0,0,0.18);
    }

    .card-title {
        font-size: 15px;
        font-weight: 700;
        margin-bottom: 18px;
        letter-spacing: 0.02em;
        text-transform: uppercase;
        color: #cdd3e0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* ============== PROFILE HEADER CARD ============== */
    .profile-hero {
        display: flex;
        align-items: center;
        gap: 22px;
        padding: 8px 4px 6px;
    }

    .profile-avatar {
        width: 92px;
        height: 92px;
        border-radius: 22px;
        object-fit: cover;
        border: 2px solid rgba(99, 102, 241, 0.4);
        box-shadow: 0 10px 28px rgba(0,0,0,0.35);
    }

    .profile-name {
        font-size: 24px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 2px;
    }

    .profile-username {
        font-size: 14.5px;
        color: #818cf8;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .profile-bio {
        font-size: 14px;
        color: #9aa2b2;
        line-height: 1.5;
        max-width: 560px;
    }

    .profile-meta {
        display: flex;
        flex-wrap: wrap;
        gap: 14px;
        margin-top: 10px;
        font-size: 13px;
        color: #7d859a;
    }

    .profile-meta span {
        display: inline-flex;
        align-items: center;
        gap: 5px;
    }

    /* ============== STAT PILLS ============== */
    .stat {
        background: rgba(255,255,255,0.035);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 20px 10px;
        text-align: center;
        transition: 0.25s ease;
    }

    .stat:hover {
        border-color: rgba(99,102,241,0.45);
        background: rgba(99,102,241,0.06);
        transform: translateY(-2px);
    }

    .stat-value {
        font-size: 26px;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff, #a5b4fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .stat-label {
        color: #838ba0;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-top: 6px;
    }

    /* Streamlit metric override (fallback stat rendering) */
    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.035);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 14px 10px;
        text-align: center;
    }

    div[data-testid="stMetricValue"] {
        color: #f3f5f9;
    }

    /* ============== DATAFRAME ============== */
    div[data-testid="stDataFrame"] {
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.08);
    }

    /* ============== DOWNLOAD BUTTONS ============== */
    .stDownloadButton > button {
        width: 100%;
        border-radius: 12px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.12);
        color: #e6e9f2;
        font-weight: 600;
        height: 46px;
        transition: 0.2s ease;
    }

    .stDownloadButton > button:hover {
        border-color: rgba(99,102,241,0.5);
        background: rgba(99,102,241,0.1);
        color: white;
    }

    /* ============== ALERTS ============== */
    div[data-testid="stAlert"] {
        border-radius: 14px;
        backdrop-filter: blur(10px);
    }

    /* ============== IMAGE ============== */
    .stImage img {
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* ============== FOOTER ============== */
    .footer {
        text-align: center;
        color: #565e70;
        margin-top: 60px;
        font-size: 12.5px;
        letter-spacing: 0.02em;
    }

    .footer span {
        color: #818cf8;
        font-weight: 600;
    }

    /* ============== ANIM ============== */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }

</style>
""", unsafe_allow_html=True)


# ==========================================
# HERO
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-badge">⚡ Python · Playwright · Streamlit</div>
    <div class="hero-icon">🐙</div>
    <h1>GitHub Profile Extractor</h1>
    <p>
        Pull public GitHub profile data, repository stats and metadata
        in seconds — clean, exportable, and ready to use.
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# INPUT
# ==========================================

st.markdown('<div class="input-wrap">', unsafe_allow_html=True)

col_input, col_btn = st.columns([3, 1], vertical_alignment="bottom")

with col_input:
    username = st.text_input(
        "GitHub Username",
        placeholder="Enter username e.g. malihamza56",
        label_visibility="collapsed"
    )

with col_btn:
    extract_clicked = st.button("🔍 Extract Profile")

st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# EXTRACT
# ==========================================

if extract_clicked:

    if not username.strip():

        st.warning("Please enter a GitHub username.")

    else:

        with st.spinner("Extracting GitHub profile... Please wait."):
            result = extract_profile(username)

        # ==================================
        # SUCCESS
        # ==================================

        if result["success"]:

            st.success("Profile extracted successfully! 🎉")

            profile = result["profile"]
            repositories = result["repositories"]
            dataframe = result["dataframe"]

            # ==================================
            # PROFILE HEADER
            # ==================================

            avatar_url = profile.get("avatar_url") or profile.get("avatar")
            name = profile.get("name") or username
            bio = profile.get("bio") or ""
            location = profile.get("location")
            company = profile.get("company")
            blog = profile.get("blog") or profile.get("website")

            st.markdown('<div class="card">', unsafe_allow_html=True)

            avatar_html = (
                f'<img class="profile-avatar" src="{avatar_url}" />'
                if avatar_url else
                '<div class="profile-avatar" style="display:flex;align-items:center;'
                'justify-content:center;font-size:32px;background:rgba(99,102,241,0.15);">🐙</div>'
            )

            meta_bits = []
            if location:
                meta_bits.append(f'<span>📍 {location}</span>')
            if company:
                meta_bits.append(f'<span>🏢 {company}</span>')
            if blog:
                meta_bits.append(f'<span>🔗 {blog}</span>')

            st.markdown(f"""
                <div class="profile-hero">
                    {avatar_html}
                    <div>
                        <div class="profile-name">{name}</div>
                        <div class="profile-username">@{username}</div>
                        <div class="profile-bio">{bio}</div>
                        <div class="profile-meta">{''.join(meta_bits)}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

            with st.expander("View raw profile JSON"):
                st.json(profile)

            # ==================================
            # REPOSITORY STATISTICS
            # ==================================

            total_repositories = repositories.get("total repositories", 0)
            followers = profile.get("followers")
            following = profile.get("following")

            st.markdown(
                '<div class="card"><div class="card-title">📊 Repository Statistics</div>',
                unsafe_allow_html=True
            )

            stat_cols = st.columns(3)

            with stat_cols[0]:
                st.markdown(f"""
                    <div class="stat">
                        <div class="stat-value">{total_repositories}</div>
                        <div class="stat-label">Repositories</div>
                    </div>
                """, unsafe_allow_html=True)

            with stat_cols[1]:
                st.markdown(f"""
                    <div class="stat">
                        <div class="stat-value">{followers if followers is not None else '—'}</div>
                        <div class="stat-label">Followers</div>
                    </div>
                """, unsafe_allow_html=True)

            with stat_cols[2]:
                st.markdown(f"""
                    <div class="stat">
                        <div class="stat-value">{following if following is not None else '—'}</div>
                        <div class="stat-label">Following</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

            # ==================================
            # REPOSITORIES
            # ==================================

            st.markdown(
                '<div class="card"><div class="card-title">📦 Repositories</div>',
                unsafe_allow_html=True
            )

            if not dataframe.empty:
                st.dataframe(dataframe, use_container_width=True, hide_index=True)
            else:
                st.info("No repositories found.")

            st.markdown('</div>', unsafe_allow_html=True)

            # ==================================
            # DOWNLOADS
            # ==================================

            st.markdown(
                '<div class="card"><div class="card-title">📥 Export Data</div>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:
                csv_bytes = dataframe.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="📊 Download CSV",
                    data=csv_bytes,
                    file_name="repositories.csv",
                    mime="text/csv"
                )

            with col2:
                json_bytes = json.dumps(profile, indent=4, ensure_ascii=False).encode("utf-8")
                st.download_button(
                    label="📄 Download JSON",
                    data=json_bytes,
                    file_name="profile.json",
                    mime="application/json"
                )

            st.markdown('</div>', unsafe_allow_html=True)

            # ==================================
            # SCREENSHOT
            # ==================================

            screenshot_path = "screenshots/profile.png"

            if os.path.exists(screenshot_path):
                st.markdown(
                    '<div class="card"><div class="card-title">📸 Profile Screenshot</div>',
                    unsafe_allow_html=True
                )
                st.image(screenshot_path, caption="Extracted GitHub Profile")
                st.markdown('</div>', unsafe_allow_html=True)

        # ==================================
        # ERROR
        # ==================================

        else:
            st.error(f"❌ Extraction failed: {result['error']}")


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    Built with Python · Playwright · Streamlit &nbsp;—&nbsp; <span>CodeWithAli</span>
</div>
""", unsafe_allow_html=True)