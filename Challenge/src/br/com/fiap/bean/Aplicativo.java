package br.com.fiap.bean;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Aplicativo {
    private Hospital hospital;
    private List<Paciente> pacientes;

    public Aplicativo(Hospital hospital) {
        this.hospital = hospital;
        this.pacientes = new ArrayList<>();
    }

    public void cadastrarPaciente(Paciente paciente) {
        pacientes.add(paciente);
    }

    public Consulta agendarConsulta(Paciente paciente, Medico medico, Date data) {
        Consulta consulta = new Consulta(data, medico, paciente);
        paciente.adicionarConsulta(consulta);
        return consulta;
    }

    public Receita emitirReceita(Paciente paciente, Medico medico, Date data, String descricao) {
        Receita receita = new Receita(data, medico, paciente, descricao);
        paciente.adicionarReceita(receita);
        return receita;
    }

    public List<Paciente> getPacientes() {
        return pacientes;
    }
}