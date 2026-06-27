def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

score = float(input("Input Score: "))
grade = get_grade(score)

if grade is None or score > 100:
    print("คะแนนไม่ถูกต้อง: ห้ามใส่เกิน 100")
else:
    print(f"เกรด = {grade}")