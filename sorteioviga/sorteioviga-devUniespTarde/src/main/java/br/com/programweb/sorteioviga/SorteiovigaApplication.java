package br.com.programweb.sorteioviga;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Classe principal que inicializa a aplicação Spring Boot.
 *
 * Aqui vemos:
 * - @SpringBootApplication que indica ao Spring que este é um projeto Boot
 *   e deve fazer o scan dos componentes (controllers, services, etc.).
 * - Método main que inicia o contexto do Spring e carrega todos os beans.
 */
@SpringBootApplication
public class SorteiovigaApplication {

	public static void main(String[] args) {
		SpringApplication.run(SorteiovigaApplication.class, args);
	}

}
