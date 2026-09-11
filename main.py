print("========================================")
print("      CLOUD COST ANALYZER")
print("========================================")

print()
print("1. Enter Cloud Usage")
print("2. Calculate Cost")
print("3. Predict Future Cost")
print("4. Optimization Recommendations")
print("5. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    print("Cloud Usage selected")

elif choice == "2":
    print("Cost Calculation selected")

elif choice == "3":
    print("Cost Prediction selected")

elif choice == "4":
    print("Optimization selected")

elif choice == "5":
    print("Thank you for using Cloud Cost Analyzer!")

else:
    print("Invalid choice")