library(tidyverse)

data <- read_delim('person_data.csv', delim = '|')

data_0_1 <- data %>%
  #converting entries to binary
  mutate(Height = !is.na(Height)) %>%
  mutate(Weight = !is.na(Weight)) %>%
  mutate(Nationality = !is.na(Nationality)) %>%
  mutate(Occupation = !is.na(Occupation)) %>%
  mutate(Alma_Mater = !is.na(Alma_Mater)) %>%
  mutate(Award = !is.na(Award)) %>%
  mutate(Spouse = !is.na(Spouse)) %>%
  mutate(Child = !is.na(Child)) %>%
  #calculate the age of participants
  filter(Birth >= 1922 & Birth < 2022) %>%
  mutate(Age = 2022 - as.numeric(Birth))

# proportion of weight entries
weight <- data_0_1 %>%
  group_by(Age, Gender) %>%
  summarise(weight = mean(Weight)) %>%
  ungroup()

# proportion of height entries
height <- data_0_1 %>%
  group_by(Age, Gender) %>%
  summarise(height = mean(Height))

# proportion of nationality entries
nationality <- data_0_1 %>%
  group_by(Age, Gender) %>%
  summarise(nationality = mean(Nationality)) %>%
  ungroup()

# proportion of occupation entries
occupation <- data_0_1 %>%
  group_by(Age, Gender) %>%
  summarise(occupation = mean(Occupation)) %>%
  ungroup()

# proportion of alma_mater entries
alma_mater <- data_0_1 %>%
  group_by(Age, Gender) %>%
  summarise(alma_mater = mean(Alma_Mater)) %>%
  ungroup()

# proportion of award entries
award <- data_0_1 %>%
  group_by(Age, Gender) %>%
  summarise(award = mean(Award)) %>%
  ungroup()

# proportion of spouse entries
spouse <- data_0_1 %>%
  group_by(Age, Gender) %>%
  summarise(spouse = mean(Spouse)) %>%
  ungroup()

# proportion of child entries
child <- data_0_1 %>%
  group_by(Age, Gender) %>%
  summarise(child = mean(Child)) %>%
  ungroup()

# Visualisations 
# weight
ggplot(data = weight) +
  aes(x = Age, y = weight, color = Gender) +
  geom_point() +
  labs(x = "Age", y = "Proportion of people with their weight mentioned") +
  scale_y_continuous(labels = scales::label_percent()) +
  theme_light()

# height
ggplot(data = height) +
  aes(x = Age, y = height, color = Gender) +
  geom_point() +
  labs(x = "Age", y = "Proportion of people with their height mentioned") +
  scale_y_continuous(labels = scales::label_percent()) +
  theme_light()

# nationality
ggplot(data = nationality) +
  aes(x = Age, y = nationality, color = Gender) +
  geom_point() +
  labs(x = "Age", y = "Proportion of people with their nationality mentioned") +
  scale_y_continuous(labels = scales::label_percent()) +
  theme_light()

# occupation
ggplot(data = occupation) +
  aes(x = Age, y = occupation, color = Gender) +
  geom_point() +
  labs(x = "Age", y = "Proportion of people with their occupation mentioned") +
  scale_y_continuous(labels = scales::label_percent()) +
  theme_light()

# alma mater
ggplot(data = alma_mater) +
  aes(x = Age, y = alma_mater, color = Gender) +
  geom_point() +
  labs(x = "Age", y = "Proportion of people with their alma_mater mentioned") +
  scale_y_continuous(labels = scales::label_percent()) +
  theme_light()

# award
ggplot(data = award) +
  aes(x = Age, y = award, color = Gender) +
  geom_point() +
  labs(x = "Age", y = "Proportion of people with their award mentioned") +
  scale_y_continuous(labels = scales::label_percent()) +
  theme_light()

# spouse
ggplot(data = spouse) +
  aes(x = Age, y = spouse, color = Gender) +
  geom_point() +
  labs(x = "Age", y = "Proportion of people with their spouse mentioned") +
  scale_y_continuous(labels = scales::label_percent()) +
  theme_light()

# children
ggplot(data = child) +
  aes(x = Age, y = child, color = Gender) +
  geom_point() +
  labs(x = "Age", y = "Proportion of people with their child mentioned") +
  scale_y_continuous(labels = scales::label_percent()) +
  theme_light()