# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 13.10202)
- **Original**: अपने-अपने घरोंको गये। हर्षसे भरे हुए ननन्‍्द बात है कि संसार मोहजालसे जकड़ा हुआ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10203)
- **Original**: और यशोदा दोनों दम्पति बालकृष्णकों गोदमें है। जैसे समुद्रमें फेन उठता और मिटता रहता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10204)
- **Original**: लेकर कुबेरभवनके समान रमणीय अपने भव्य है, उसी प्रकार इस भवसागरमें मनुष्योंको संयोग
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10205)
- **Original**: भवनमें रहने लगे। इस प्रकार वे दोनों बालक और वियोगका अनुभव होता रहता है।!'
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10206)
- **Original**: शुक्लपक्षके चन्द्रमाकी कलाकी भाँति बढ़ने लगे। गर्गकी यह बात सुनकर नन्‍्दजी उदास हो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10207)
- **Original**: अब वे गौओंकी पूँछ और दीवाल पकड़कर खड़े गये; क्योंकि साधु पुरुषोंक लिये सत्पुरुषोंका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10208)
- **Original**: होने लगे। प्रतिदिन आधा शब्द या चौथाई शब्द वियोग मरणसे भी अधिक कष्टदायक होता है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10209)
- **Original**: बोल पाते थे। मुने! आँगनमें चलते हुए बे दोनों सम्पूर्ण शिष्योंसे घिरे हुए मुनिवर गर्ग जब जानेको
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10210)
- **Original**: भाई माता-पिताका हर्थ बढ़ाने लगे। अब बालक उद्यत हुए, तब रोते हुए नन्द आदि सब गोप-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10211)
- **Original**: श्रीहरि दो-एक पग चलनेमें समर्थ हो गये। घरमें गोपियोंने अत्यन्त प्रौतिपूर्वक विनीतभावसे उन्हें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10212)
- **Original**: और आँगनमें वे घुटनोंके बलसे चलने-फिरने प्रणाम किया। उन सबको आशीर्वाद देकर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10213)
- **Original**: लगे। संकर्षणकी अवस्था बालक श्रीकृष्णसे एक मुनिश्रेष्ठ गर्ग साननद मथुराकों पधारे। ऋषि-मुनि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10214)
- **Original**: साल अधिक थी। वे दोनों भाई माता-पिताका तथा प्रिय बन्धुवर्ग सभी धनसे सम्पन्न हो प्रसन्न-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10215)
- **Original**: आनन्दवर्धन करते हुए दिन-दिन बड़े होने लगे।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10216)
- **Original**: + श्रीकृष्णजन्मखण्ड * 459 £5564446444 64% 44 5555 44444 446 #% 6 # 44 8 55556 $# 4 # 4 # 6 8 # # ## % 5 $ फ इ ऊ/ऊ ऊ ह# 866 88 68% ##% मायासे शिशुरूपधारी वे दोनों बालक गोकुलमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10217)
- **Original**: गृहमें निवास करने लगे। नारद! जिस कल्पमें यह विचरते हुए अच्छी तरह चलनेमें समर्थ हो गये।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10218)
- **Original**: कथा घटित हुई थी, उस समय तुम पचास अब बे स्फुट वाक्य बोल लेते थे। कामिनियोंके पति गन्धर्वराज उपबर्हणके नामसे मुने! गर्गजी मधथुरामें वसुदेवजीके घर गये।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10219)
- **Original**: प्रसिद्ध थे। वे सब सुन्दरियाँ तुम्हें प्राणोंसे बढ़कर उन्होंने पुरोहितजीको प्रणाम किया और अपने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10220)
- **Original**: प्रिय मानती थीं और तुम श्रृज्वारमें निपुण नवयुवक दोनों पुत्रोंका कुशल-समाचार पूछा। गर्गजीने थे। तदनन्तर ब्रह्माजीके शापसे एक द्विजको उनका कुशल-मज़ल सुनाया और नामकरण-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10221)
- **Original**: दासीके पुत्र हुए। उसके बाद बैष्णवोंकी जूठन संस्कारके महान्‌ उत्सवकी चर्चा की। वह सब
- **Translation**: 

---

