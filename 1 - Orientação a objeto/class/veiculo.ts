class Veiculo {
  _id: Number;
  velocidade: number;
  modelo: String;
  cor: String;

  constructor(velocidade: number, modelo: String, cor: String) {
    this.velocidade = velocidade;
    this.modelo = modelo;
    this.cor = cor;
  }

  get id(){
    return this._id
  }
}

export default Veiculo;
