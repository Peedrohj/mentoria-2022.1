import Veiculo from "../class/veiculo";

const carroAmarelo: Partial<Veiculo> = {
  id: 1,
  cor: "Amarelo",
  modelo: "Palio",
  velocidade: 10,
};

const carroAzul: Veiculo = new Veiculo(10, "Gol", "Azul");
const carroPreto: Veiculo = new Veiculo(10, "Celta", "Preto");

carroAmarelo.velocidade = 20;
carroAzul.velocidade = 40;
carroPreto.velocidade = 60;
