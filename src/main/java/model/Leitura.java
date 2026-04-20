package model;

public class Leitura {
    private int id;
    private double temperatura;
    private double umidade;
    
    public Leitura(int id, double temperatura, double umidade) {
        this.id = id;
        this.temperatura = temperatura;
        this.umidade = umidade;
    }

    public int getId() { return id; }
    public double getTemperatura() { return temperatura; }
    public double getUmidade() { return umidade; }
}