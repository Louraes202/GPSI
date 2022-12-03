using MOD09_Exer5;

Produto p1 = new Produto();

Console.WriteLine("Digite o preço do custo: ");
p1.change_precoCusto(Double.Parse(Console.ReadLine()));
Console.WriteLine("Digite o preço do venda: ");
p1.change_precoVenda(Double.Parse(Console.ReadLine()));


Console.WriteLine("Preço de custo: {0}", p1.getPrecoCusto());
Console.WriteLine("Preço de custo: {0}", p1.getPrecoVenda());
Console.WriteLine("Margem de lucro: {0}", p1.calcularMargemLucro());
Console.WriteLine("Margem de lucro em percentagem: {0}%", p1.getMargemLucroPercentagem());