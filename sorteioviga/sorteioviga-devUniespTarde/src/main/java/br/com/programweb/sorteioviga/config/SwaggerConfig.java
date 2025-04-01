package br.com.programweb.sorteioviga.config;

import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.OpenAPI;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SwaggerConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info().title("API Sorteio Viga")
                        .title("API Sorteio Viga")
                        .version("v1")
                        .description("Documentação da API para o sistema de sorteio semanal...")
                );
    }
}
