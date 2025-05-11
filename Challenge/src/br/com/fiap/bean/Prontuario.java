package br.com.fiap.bean;

import java.util.ArrayList;
import java.util.List;

public class Prontuario {
    private String numero;
    private List<Consulta> consultas;
    private List<Receita> receitas;

    public Prontuario(String numero) {
        this.numero = numero;
        this.consultas = new ArrayList<>();
        this.receitas = new ArrayList<>();
    }

    public void adicionarConsulta(Consulta consulta) {
        consultas.add(consulta);
    }

    public void adicionarReceita(Receita receita) {
        receitas.add(receita);
    }

    public String getNumero() {
        return numero;
    }

    public List<Consulta> getConsultas() {
        return consultas;
    }

    public List<Receita> getReceitas() {
        return receitas;
    }
}