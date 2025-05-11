package br.com.fiap.bean;

import java.util.Date;

public class Receita {
    private Date data;
    private Medico medico;
    private Paciente paciente;
    private String descricao;

    public Receita(Date data, Medico medico, Paciente paciente, String descricao) {
        this.data = data;
        this.medico = medico;
        this.paciente = paciente;
        this.descricao = descricao;
    }

    public Date getData() {
        return data;
    }

    public Medico getMedico() {
        return medico;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public String getDescricao() {
        return descricao;
    }
}