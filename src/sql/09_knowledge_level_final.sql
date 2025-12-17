INSERT INTO public.knowledge_level
(id, created_at, modified_at, name, description, value, polymorphic_ctype_id)
VALUES
(1,'2022-04-20 23:34:40.347564+00','2022-04-20 23:34:55.638663+00','Nenhum','não conhece o tema',1, 39),
(2,'2022-04-20 23:35:10.668466+00','2022-04-23 00:00:04.307148+00','Baixo','conhecimento pela  leitura de materiais ou em curso de curta duração (até 4 horas)',0, 39),
(3,'2022-04-20 23:35:29.161251+00','2022-04-23 00:00:17.524553+00','Moderado','conhecimento por disciplina, projeto de graduação ou Iniciação Científica no tema, ou   curso com duração superior a 4 horas;',3, 39),
(4,'2022-04-20 23:35:40.745633+00','2022-04-23 00:00:23.305717+00','Alto','é especialista no tema, tem certificação ou desenvolveu pesquisa de mestrado ou doutorado.',5, 39);