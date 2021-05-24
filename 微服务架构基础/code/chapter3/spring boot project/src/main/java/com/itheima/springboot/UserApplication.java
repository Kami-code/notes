package com.itheima.springboot;
import org.apache.activemq.command.ActiveMQQueue;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Bean;

import javax.jms.Queue;


@SpringBootApplication
@EnableCaching
public class UserApplication {
    public static void main(String[] args) {
        SpringApplication.run(com.itheima.springboot.UserApplication.class, args);
    }
    @Bean
    public Queue queue() {
        return new ActiveMQQueue("active.queue");
    }
}
