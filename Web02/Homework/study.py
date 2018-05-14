# Exe1
# Are there any duplicate ids in the records?
# If no, why? Guess what information this is field represents and its implication/application
# Không có id nào trùng nhau vì mỗi _id đại diện cho một trường thông tin.

# Exe2
Service.objects.get(id ="5af86215846ee804c0ce7fd1")

# Exe3
Service.objects.get(id="5af86215846ee804c0ce7fd1").delete()
