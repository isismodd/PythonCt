package br.com.fiap.bean;

import java.util.ArrayList;
import java.util.List;

public class Unidade {
    private String nome;
    private String endereco;
    private List<Medico> medicos;

    public Unidade(String nome, String endereco) {
        this.nome = nome;
        this.endereco = endereco;
        this.medicos = new ArrayList<>();
    }

    public void adicionarMedico(Medico medico) {
        medicos.add(medico);
    }

    public String getNome() {
        return nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public List<Medico> getMedicos() {
        return medicos;
    }
}