#!/usr/bin/env python3
"""Generate a professional 1-page resume PDF matching the portfolio content.
Uses the same data as the updated resume.tex (LaTeX source of truth).
"""

from fpdf import FPDF
from fpdf.enums import XPos, YPos


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="in", format="letter")
        self.set_auto_page_break(auto=True, margin=0.28)

        # System fonts with good Unicode coverage (available on this Arch system)
        dejavu = "/usr/share/fonts/TTF/DejaVuSans.ttf"
        dejavu_bold = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
        self.add_font("DejaVu", "", dejavu)
        self.add_font("DejaVu", "B", dejavu_bold)

        self.accent = (15, 118, 110)      # #0F766E teal (matches portfolio + original tex)
        self.text_dark = (55, 65, 81)     # #374151
        self.text_black = (20, 20, 20)

    def header_section(self):
        # Name
        self.set_font("DejaVu", "B", 17)
        self.set_text_color(*self.text_black)
        self.cell(0, 0.26, "Saarthak Saxena", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Contact line
        self.set_font("DejaVu", "", 7)
        self.set_text_color(*self.text_dark)
        contact = "saarthaksaxena7@gmail.com   •   linkedin.com/in/saarthakiiitd   •   github.com/Saarthakkj   •   x.com/curlysaarthak"
        self.cell(0, 0.17, contact, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.07)

    def section_title(self, title: str):
        self.set_font("DejaVu", "B", 9.5)
        self.set_text_color(*self.accent)
        self.cell(0, 0.17, title.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Accent underline
        self.set_draw_color(*self.accent)
        self.set_line_width(0.014)
        y = self.get_y() + 0.005
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(0.055)

    def job_header(self, role: str, date: str, company: str, extra: str = ""):
        y = self.get_y()
        # Role left + date right on line 1
        self.set_font("DejaVu", "B", 7.5)
        self.set_text_color(*self.text_dark)
        date_w = self.get_string_width(date) + 0.02
        self.set_xy(self.w - self.r_margin - date_w, y)
        self.cell(date_w, 0.145, date, align="R")

        self.set_font("DejaVu", "B", 8.8)
        self.set_text_color(*self.text_black)
        self.set_xy(self.l_margin, y)
        avail = self.w - self.r_margin - self.l_margin - date_w - 0.12
        self.cell(avail, 0.145, role)
        self.ln(0.155)

        # Company line (with optional extra right)
        y2 = self.get_y()
        if extra:
            self.set_font("DejaVu", "", 7.2)
            self.set_text_color(*self.text_dark)
            extra_w = self.get_string_width(extra) + 0.02
            self.set_xy(self.w - self.r_margin - extra_w, y2)
            self.cell(extra_w, 0.13, extra, align="R")
        else:
            extra_w = 0

        self.set_font("DejaVu", "", 7.8)
        self.set_text_color(*self.text_dark)
        self.set_xy(self.l_margin, y2)
        avail2 = self.w - self.r_margin - self.l_margin - extra_w - 0.1
        self.cell(avail2, 0.13, company)
        self.ln(0.14)

    def bullet(self, text: str):
        self.set_font("DejaVu", "", 7.6)
        self.set_text_color(*self.text_black)
        bullet = "•  "
        self.set_x(self.l_margin + 0.08)
        # multi_cell handles wrapping automatically
        self.multi_cell(
            w=0,
            h=0.122,
            text=bullet + text,
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )
        self.ln(0.008)

    def project_header(self, title: str, meta: str):
        y = self.get_y()
        # Right meta first
        self.set_font("DejaVu", "", 7.2)
        self.set_text_color(*self.text_dark)
        meta_w = self.get_string_width(meta) + 0.01
        self.set_xy(self.w - self.r_margin - meta_w, y)
        self.cell(meta_w, 0.135, meta, align="R")

        # Then title from left on same line
        self.set_font("DejaVu", "B", 8.6)
        self.set_text_color(*self.text_black)
        self.set_xy(self.l_margin, y)
        avail = self.w - self.r_margin - self.l_margin - meta_w - 0.1
        self.cell(avail, 0.135, title)
        self.set_xy(self.l_margin, y + 0.135)
        self.ln(0.0)  # ensure y advanced

    def project_bullet(self, text: str):
        self.set_font("DejaVu", "", 7.5)
        self.set_text_color(*self.text_black)
        self.set_x(self.l_margin + 0.08)
        self.multi_cell(
            w=0,
            h=0.118,
            text="•  " + text,
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )
        self.ln(0.006)

    def education_entry(self, degree: str, date: str, school: str):
        # Clean stacked layout (reliable, no positioning tricks)
        self.set_font("DejaVu", "B", 8.6)
        self.set_text_color(*self.text_black)
        self.cell(0, 0.135, degree, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font("DejaVu", "B", 7.5)
        self.set_text_color(*self.text_dark)
        self.cell(0, 0.12, date, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font("DejaVu", "", 7.8)
        self.set_text_color(*self.text_dark)
        self.cell(0, 0.12, school, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def main():
    pdf = ResumePDF()
    pdf.set_margins(left=0.42, top=0.30, right=0.42)
    pdf.add_page()

    # === HEADER ===
    pdf.header_section()

    # === EXPERIENCE ===
    pdf.section_title("Experience")

    # Brace.so
    pdf.job_header("Applied AI Intern", "Mar 2026 – May 2026", "Brace.so")
    pdf.bullet("Pedro (Autonomous KG Agent): Built multi-LLM autonomous agent (Gemini + Claude) maintaining 10K+ node knowledge graph with zero manual curation. Uses parallel evaluation, deferred decisions for low-confidence cases, semantic similarity for evidence ranking, and parent-child taxonomy classification.")
    pdf.bullet("Search Engine: Rebuilt people search ranking with LLM-generated structured constraints (xAI/Grok), replacing fuzzy matching with deterministic exact-match gating for role, company, and location.")
    pdf.bullet("Oden (Connection Path Discovery): Built multi-hop pathfinding across 4,739 actors and 11,609 edges. Evaluated 3.4M+ directed trials and 29.3M route combos; achieved 99.87% success rate across 9 strategies.")
    pdf.bullet("Actor-Relationship Optimization: Designed scoring via 60+ experiments reducing processed data to 2.93% of baseline (72 profiles, ~90K records) while retaining 98% high-quality edges. Cut external API calls ~60% via single-pass consolidation.")
    pdf.bullet("Knowledge Graph Visualizer: Built full-stack interactive visualizer for exploring and debugging the live 10K+ node graph.")
    pdf.ln(0.025)

    # Stealth Startup
    pdf.job_header("ML Engineer", "Jun 2025 – Nov 2025", "Stealth Startup", "Contract: Jul 2025 – Oct 2025")
    pdf.bullet("Novel GNN from Scratch: Trained GNN from zero on novel pharmachemistry task + dataset + model under $35 budget. No pretrained weights, no reference implementations, no existing benchmarks.")
    pdf.bullet("Experimentation at Scale: Extended GraphGym for 48k data points. Orchestrated 1,000,000+ optimization trials on distributed GPUs and beat Chemprop, the industry standard.")
    pdf.bullet("Production Delivery: Shipped lightweight 2M-param inference API in 8 weeks (full lifecycle: data ingestion to FastAPI + Docker + AWS deployment).")
    pdf.bullet("Business Impact: Client used this work to secure a INR 30 Lac (~$35k) research grant.")
    pdf.ln(0.025)

    # HeydoTech
    pdf.job_header("Software Engineering Intern", "Jan 2024 – May 2024", "HeydoTech")
    pdf.bullet("Developed 2 automation tools using OpenCV and PyAutoGUI for internal projects.")
    pdf.bullet("Collaborated with cross-functional teams of 5+ to ship feature enhancements improving performance for ~100 users.")
    pdf.bullet("Delivered UI/UX improvements with positive feedback from 80% of test users.")

    # === PROJECTS ===
    pdf.section_title("Projects")

    pdf.project_header("Docbook", "Python, GraphRAG, CLI  |  Apr 2025 – Present")
    pdf.project_bullet("GraphRAG-based CLI tool for intelligent documentation context extraction from single URL input.")
    pdf.project_bullet("Converts URL to full knowledge graph using crawl4ai with automated semantic search and retrieval.")
    pdf.ln(0.018)

    pdf.project_header("Bayesian Course Recommendation System", "Python, PyTorch, Bayesian ML  |  2025")
    pdf.project_bullet("Achieved 0.915 AUC using Bayesian Personalized Ranking (BPR) for implicit feedback recommendations.")
    pdf.project_bullet("Matrix factorization with BPR optimization and probabilistic handling for cold-start problem.")

    # === EDUCATION ===
    pdf.section_title("Education")
    pdf.education_entry(
        "BTech, Electronics and Communication Engineering",
        "Nov 2022 – Present",
        "IIIT Delhi"
    )

    # Write output (overwrite)
    output_path = "resume.pdf"
    pdf.output(output_path)
    print(f"✓ Generated {output_path} (1 page, matching current portfolio content)")


if __name__ == "__main__":
    main()
