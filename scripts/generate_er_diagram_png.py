import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_er_diagram():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
    ax.set_facecolor("#FFFFFF")
    fig.patch.set_facecolor("#FFFFFF")

    # Draw entity box helper
    def draw_entity(x, y, w, h, title, pk_list, attr_list):
        # Header Box
        header_rect = patches.FancyBboxPatch(
            (x, y + h - 0.45), w, 0.45,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor="#A51C30", edgecolor="#A51C30", linewidth=1.5
        )
        ax.add_patch(header_rect)
        ax.text(x + w/2, y + h - 0.22, title, color="white", weight="bold", fontsize=11, ha="center", va="center", fontfamily="sans-serif")
        
        # Body Box
        body_rect = patches.FancyBboxPatch(
            (x, y), w, h - 0.45,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor="#F9FAFB", edgecolor="#BFBFBF", linewidth=1
        )
        ax.add_patch(body_rect)

        # Draw attributes
        curr_y = y + h - 0.7
        for pk in pk_list:
            ax.text(x + 0.15, curr_y, "[PK] " + pk, color="#A51C30", weight="bold", fontsize=9, va="center", fontfamily="sans-serif")
            curr_y -= 0.28
        
        for attr in attr_list:
            ax.text(x + 0.15, curr_y, "• " + attr, color="#151514", fontsize=8.5, va="center", fontfamily="sans-serif")
            curr_y -= 0.26

    # 1. Employees Entity
    draw_entity(0.5, 2.5, 3.2, 3.8, "EMPLOYEES (Master Dim)", 
                ["employee_id: VARCHAR(10) [PK]"],
                ["full_name: VARCHAR(100)", "department: VARCHAR(50)", "job_role: VARCHAR(50)", 
                 "experience_years: REAL", "location: VARCHAR(50)", "pre_rating: REAL", "retention_risk: VARCHAR(20)"])

    # 2. Training Records Entity
    draw_entity(4.4, 1.2, 3.6, 5.2, "TRAINING_RECORDS (Fact)",
                ["record_id: INTEGER [PK]"],
                ["employee_id: VARCHAR(10) [FK]", "training_type: VARCHAR(50)", "program_name: VARCHAR(100)",
                 "delivery_mode: VARCHAR(20)", "duration_days: INT", "training_cost: REAL",
                 "pre_score: REAL", "post_score: REAL", "score_delta: REAL [CALC]",
                 "post_rating: REAL", "rating_diff: REAL [CALC]", "feedback_score: REAL", "completion_date: DATE"])

    # 3. Users Entity
    draw_entity(8.6, 4.2, 2.8, 2.6, "USERS (Auth Dim)",
                ["user_id: INT [PK]"],
                ["username: VARCHAR(50)", "password_hash: VARCHAR(255)", "salt: VARCHAR(64)", "role: VARCHAR(30)"])

    # 4. Active Sessions Entity
    draw_entity(8.6, 0.8, 2.8, 2.6, "ACTIVE_SESSIONS",
                ["session_token: VARCHAR(64) [PK]"],
                ["user_id: INT [FK]", "username: VARCHAR(50)", "role: VARCHAR(30)", "last_active: TIMESTAMP"])

    # Connectors with arrows
    # employees -> training_records
    ax.annotate("", xy=(4.4, 3.8), xytext=(3.7, 3.8),
                arrowprops=dict(arrowstyle="->", color="#A51C30", lw=2, mutation_scale=15))
    ax.text(4.05, 4.0, "1 : N\n(enrolled)", color="#A51C30", weight="bold", fontsize=9, ha="center")

    # users -> active_sessions
    ax.annotate("", xy=(10.0, 3.4), xytext=(10.0, 4.2),
                arrowprops=dict(arrowstyle="->", color="#A51C30", lw=2, mutation_scale=15))
    ax.text(10.3, 3.8, "1 : N\n(session)", color="#A51C30", weight="bold", fontsize=9, ha="left")

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    plt.title("ABES Engineering College — Training Effectiveness Analytics ER Diagram", 
              fontsize=14, weight="bold", color="#A51C30", pad=20, fontfamily="sans-serif")
    plt.tight_layout()
    plt.savefig("docs/09_ER_Diagram.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: docs/09_ER_Diagram.png")

if __name__ == "__main__":
    draw_er_diagram()
