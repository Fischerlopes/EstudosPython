salary = float(input('Digite seu salário : '))

if salary <= 1250:
    newsalary = salary * 1.15
    print('Seu novo salário será R$ : {:.2f}'.format(newsalary))
else:
    newsalary = salary * 1.10
    print('Seu novo salário será R$ : {:.2f}'.format(newsalary))
