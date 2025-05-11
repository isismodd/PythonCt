package br.com.fiap.bean;

import java.util.ArrayList;
import java.util.List;

public class Hospital {
    private String nome;
    private List<Unidade> unidades;

    public Hospital(String nome) {
        this.nome = nome;
        this.unidades = new ArrayList<>();
    }

    public void adicionarUnidade(Unidade unidade) {
        unidades.add(unidade);
    }

    public String getNome() {
        return nome;
    }

    public List<Unidade> getUnidades() {
        return unidades;
    }
}