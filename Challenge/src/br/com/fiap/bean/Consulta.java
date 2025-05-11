package br.com.fiap.bean;

import java.util.Date;

public class Consulta {
    private Date data;
    private Medico medico;
    private Paciente paciente;
    private String diagnostico;

    public Consulta(Date data, Medico medico, Paciente paciente) {
        this.data = data;
        this.medico = medico;
        this.paciente = paciente;
    }

    public void setDiagnostico(String diagnostico) {
        this.diagnostico = diagnostico;
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

    public String getDiagnostico() {
        return diagnostico;
    }
}