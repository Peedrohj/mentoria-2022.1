interface Iveiculo {
  _id?: Number ;
  velocidade: number;
  modelo: String;
  cor: String;
}

class Veiculo {
  _id: Number;
  velocidade: number;
  modelo: String;
  cor: String;

  constructor(params: Iveiculo) {
    this.velocidade = params.velocidade;
    this.modelo = params.modelo;
    this.cor = params.cor;
  }

  get id() {
    return this._id;
  }
}

export default Veiculo;
