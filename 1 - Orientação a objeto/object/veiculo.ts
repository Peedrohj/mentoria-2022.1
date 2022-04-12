import Veiculo from "../class/veiculo";

const carroAmarelo: Partial<Veiculo> = {
  id: 1,
  cor: "Amarelo",
  modelo: "Palio",
  velocidade: 10,
};

const carroAzul: Veiculo = new Veiculo({
  modelo: "Gol",
  velocidade: 12,
  cor: "Amarelo",
});
const carroPreto: Veiculo = new Veiculo({
  modelo: "Celta",
  velocidade: 10,
  cor: "Preto",
});

carroAmarelo.velocidade = 20;
carroAzul.velocidade = 40;
carroPreto.velocidade = 60;
