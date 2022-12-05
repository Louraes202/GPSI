using MOD9_Exer4;
List<double> salarios = new List<double>();

Console.WriteLine("DINO Ltda.");

// Declaração dos empregados
Empregado E1 = new Empregado("Martim", 4300);
Empregado E2 = new Empregado("Joana", 1500);
Empregado E3 = new Empregado("Antonio", 800);
Empregado E4 = new Empregado("Rodrigo", 950);
Empregado E5 = new Empregado("Laura", 3100);

// Lista de objetos (substitui a classe da empresa)
List<Empregado> Empregados = new List<Empregado>() { E1, E2, E3, E4, E5 };

// Atribuição de todos os salários a uma lista
foreach(Empregado empregado in Empregados)
{
    salarios.Add(empregado.Salario());
}

// var
double maxSalario = salarios.Max();
double medioSalario = salarios.Average();
string maxEmpregado = "";

// Verificação do empregado mais bem pago
foreach(Empregado empregado in Empregados)
{
    if(empregado.Salario() == maxSalario) {
        maxEmpregado = empregado.Nome();
    }
}

Console.WriteLine("Max salario:" + maxSalario);
Console.WriteLine("Max empregado: " + maxEmpregado);
Console.WriteLine("Medio salario: " + medioSalario);



