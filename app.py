import streamlit as st

# 1. 페이지 설정 (모바일 최적화 레이아웃)
st.set_page_config(
    page_title="리버파크자이 입주민 긴급 안내",
    page_icon="🚨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 커스텀 CSS (모바일 가독성 및 디자인 강화)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap');
    
    /* 전체 폰트 및 배경 설정 */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Noto Sans KR', sans-serif;
        background-color: #f8fafc;
        color: #1e293b;
    }
    
    /* 헤더 카드 스타일 */
    .header-card {
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
        color: white;
        padding: 24px 16px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        text-align: center;
    }
    .header-card h4 {
        color: #93c5fd;
        font-weight: 700;
        font-size: 1rem;
        margin-top: 0px;
        margin-bottom: 8px;
    }
    .header-card h2 {
        font-weight: 900;
        line-height: 1.3;
        font-size: 1.4rem;
        margin-top: 0px;
        margin-bottom: 12px;
    }
    .header-card p {
        font-size: 0.85rem;
        opacity: 0.85;
        margin: 0px;
    }
    
    /* 긴급 경고 카드 스타일 */
    .danger-card {
        background-color: #fef2f2;
        border-left: 5px solid #ef4444;
        border-right: 1px solid #fee2e2;
        border-top: 1px solid #fee2e2;
        border-bottom: 1px solid #fee2e2;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .danger-card-title {
        color: #b91c1c;
        font-weight: 800;
        font-size: 1.05rem;
        margin-bottom: 8px;
    }
    
    /* 정보 요약 섹션 제목 */
    .section-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-top: 28px;
        margin-bottom: 12px;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 6px;
    }
    
    /* 미니 통계/수치 카드 */
    .metric-card {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 12px 6px;
        text-align: center;
        box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
    }
    .metric-val {
        font-size: 1.25rem;
        font-weight: 900;
        color: #b91c1c;
    }
    .metric-label {
        font-size: 0.75rem;
        color: #64748b;
        margin-top: 4px;
        line-height: 1.3;
    }
    
    /* 모바일 맞춤 사건 경위 카드 */
    .flow-card {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
    }
    .flow-tag {
        font-size: 0.75rem;
        font-weight: 700;
        color: #1e3a8a;
        background-color: #dbeafe;
        padding: 2px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 6px;
    }
    .flow-tag.danger {
        color: #b91c1c;
        background-color: #fee2e2;
    }
    .flow-title {
        font-weight: 700;
        font-size: 0.95rem;
        color: #0f172a;
        margin-bottom: 6px;
    }
    .flow-desc {
        font-size: 0.85rem;
        line-height: 1.5;
        color: #334155;
    }
    
    /* 버튼 스타일 전반 커스텀 */
    div.stLinkButton > a {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        height: 52px !important;
        background: linear-gradient(90deg, #ef4444 0%, #dc2626 100%) !important;
        color: white !important;
        font-size: 1.05rem !important;
        font-weight: 800 !important;
        border-radius: 8px !important;
        text-decoration: none !important;
        box-shadow: 0 4px 10px rgba(239, 68, 68, 0.3) !important;
        border: none !important;
        transition: transform 0.1s ease-in-out;
    }
    div.stLinkButton > a:active {
        transform: scale(0.98);
    }
    
    /* 푸터 스타일 */
    .footer {
        text-align: center;
        padding: 20px 0;
        font-size: 0.75rem;
        color: #64748b;
        border-top: 1px solid #e2e8f0;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 메인 콘텐츠
# 상단 타이틀 카드
st.markdown("""
<div class="header-card">
    <h4>공동재산(장기수선충당금) 보호를 위한</h4>
    <h2>외부감사 요청 입주민 동의 안내</h2>
    <p>발신: 108동대표 진상호, 109동대표 김윤숙, 111동대표 이종혁, 113동대표 김재중</p>
</div>
""", unsafe_allow_html=True)

# 모바일 화면을 위해 바로 온라인 동의서 작성 링크 제공 (최상단 노출)
st.markdown("### 📝 온라인 감사 동의서 작성")
st.link_button("👉 1분 완성 모바일 동의서 작성하기", "https://forms.gle/z8gMe56HSBmYUso19")

st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# 🚨 실제 피해 상황 요약
st.markdown("""
<div class="danger-card">
    <div class="danger-card-title">🚨 현재 발생한 실제 입주민 피해</div>
    <div style="font-size: 0.9rem; line-height: 1.6; color: #1e293b;">
        전임 회장의 독단적인 계약 조건 변경으로 인해 <strong>장기수선충당금 13.3억 원 강제 인출 완료</strong><br>
        <span style="font-size: 0.8rem; color: #64748b;">(농협 9.3억 + 신한 4억, 지연이자 약 2,800만 원 포함)</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 수치 메트릭 카드 레이아웃
st.markdown("<div class='section-title'>📊 3대 외상공사 계약 총액 (51.4억)</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-val">6.6억</div>
        <div class="metric-label">(주)수산기업<br>환경개선공사</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="metric-card" style="border: 1.5px solid #ef4444; background-color: #fff5f5;">
        <div class="metric-val" style="color: #ef4444;">13억</div>
        <div class="metric-label" style="font-weight:700; color: #b91c1c;">(주)세원<br>시설물보수 (유출)</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-val">31.8억</div>
        <div class="metric-label">(주)LK개발<br>지하주차장 도색</div>
    </div>
    """, unsafe_allow_html=True)

# 💡 사건 경위
st.markdown("<div class='section-title'>🔍 핵심 사건 경위 — 무슨 일이 있었나?</div>", unsafe_allow_html=True)

st.markdown("""
<div class="flow-card">
    <div class="flow-tag">1. 배경</div>
    <div class="flow-title">100억 하자보수 소송 진행 중 (미확정)</div>
    <div class="flow-desc">시공사(GS건설) 대상 약 100억 규모 손해배상 소송 진행 중이며 승소 여부·판결금 수령액 모두 미확정 상태에서, 이 미확정 판결금을 재원으로 삼아 외상공사 계약들을 강행했습니다.</div>
</div>

<div class="flow-card" style="border-left: 4px solid #ef4444;">
    <div class="flow-tag danger">2. 핵심 문제</div>
    <div class="flow-title">전임 회장, 계약 조건 독단 변경</div>
    <div class="flow-desc">전임 회장이 계약 조건을 <strong>"소송 승소 후 지급"에서 "2026년 1월 지급"으로 독단적으로 변경</strong>하였습니다. 타 동대표들은 이 변경 사실을 전혀 몰랐습니다.</div>
</div>

<div class="flow-card" style="border-left: 4px solid #ef4444;">
    <div class="flow-tag danger">3. 결과</div>
    <div class="flow-title">장기수선충당금 13.3억 원 강제 유출</div>
    <div class="flow-desc">법원의 지급명령에 대해 현 입대의가 이의신청을 포기하여 농협/신한 계좌에서 <strong>13.3억 원이 강제 인출</strong>되었습니다. 이후 현 입대의(8인)는 <strong>배임 혐의 전임 회장과 약 2,800만 원에 불법 합의(민/형사 면책 포함)를 강행</strong>하여 청구권을 영구 포기했습니다.</div>
</div>

<div class="flow-card">
    <div class="flow-tag">4. 추가 위험</div>
    <div class="flow-title">(주)LK개발 31.8억 지하주차장 도색공사 미지급</div>
    <div class="flow-desc">LK개발의 31.8억 원 외상공사 대금 역시 미지급 상태입니다. 소송 패소나 판결금 부족 시 추가 강제집행의 위험이 있으며, 2,529세대 기준 <strong>세대당 수백만 원의 추가 분담금</strong>이 발생할 수 있습니다.</div>
</div>
""", unsafe_allow_html=True)

# 외부감사 필요성 강조
st.markdown("""
<div class="danger-card" style="background-color: #fffbeb; border-left: 5px solid #f59e0b; border-color: #f59e0b;">
    <div class="danger-card-title" style="color: #b45309;">⚠ 왜 지금 외부감사를 요청해야 하나요?</div>
    <div style="font-size: 0.85rem; line-height: 1.6; color: #78350f;">
        입주민 공동 재산이 강제 인출되는 초유의 사태에도 불구하고, 현 입대의 8인은 입주민 동의 및 법률 자문 없이 전임 회장과 <strong>불법 합의를 하고 면책</strong>해 주었습니다.<br>
        충당금 강제인출 사태와 불법 합의에 대한 <strong>철저한 객관적 조사</strong>를 위해 도청·시청 등 외부기관 감사가 반드시 필요합니다.
    </div>
</div>
""", unsafe_allow_html=True)

# KBS 뉴스 보도 영상
st.markdown("<div class='section-title'>📺 KBS 뉴스 보도 영상</div>", unsafe_allow_html=True)
st.video("https://youtu.be/X6Z9xzlS8G4?si=OIQrouIc2nwIQr4o")

# 한 번 더 하단에 동의서 링크 배치
st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)
st.link_button("👉 지금 감사 동의서 작성하러 가기", "https://forms.gle/z8gMe56HSBmYUso19")

# 푸터
st.markdown("""
<div class="footer">
    <p>리버파크자이아파트 입주민 협의체 | 2026년 6월 30일</p>
    <p style="font-size: 0.7rem; opacity: 0.8; margin-top: 4px;">본 페이지는 공동주택관리법 제27조에 의거한 감사 권한 행사의 일환으로 제공됩니다.</p>
</div>
""", unsafe_allow_html=True)
