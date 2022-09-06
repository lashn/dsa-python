try:
  print(10 / 0)
  print(1)
except Exception as e:
  print(f"exception excepted: {e}")
print("next operation")

# #next operation will not execute so better use exp handinling
# print(10 / 0)
# print("next operation")