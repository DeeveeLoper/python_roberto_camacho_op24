from read_data import read_data

df = read_data()

approved = df.query("Beslut == 'Beviljad'")
#approvet = df[df["Beslut"] == "Bevilja"]

number_approved =len(approved)
total_applications = len(df)
approved_precentage = number_approved/total_applications

if __name__ == '__main__':
    # for testing purpose
    print(number_approved)
    print(total_applications)
    print(approved_precentage)
