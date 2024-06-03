package pt41_Implementacio_Classes;

public class Ex4_centreCultural {

	public static void main(String[] args) {

	}

}

class Material{
	private int id;
	private String titol;
	private String autor;
	
	public Material() {
		super();
	}

	public Material(int id, String titol, String autor) {
		super();
		this.id = id;
		this.titol = titol;
		this.autor = autor;
	}

	public int getId() {
		return id;
	}

	public String getTitol() {
		return titol;
	}

	public String getAutor() {
		return autor;
	}
}

class Disc extends Material{
	private String nom_discografia;

	public Disc() {
		super();
	}

	public Disc(int id, String titol, String autor, String nom_discografia) {
		super(id, titol, autor);
		this.nom_discografia = nom_discografia;
	}

	public String getNom_discografia() {
		return nom_discografia;
	}
}

class Llibre extends Material{
	private int numero_pagines;

	public Llibre() {
		super();
		
	}

	public Llibre(int id, String titol, String autor, int numero_pagines) {
		super(id, titol, autor);
		this.numero_pagines = numero_pagines;
	}

	public int getNumero_pagines() {
		return numero_pagines;
	}
}
