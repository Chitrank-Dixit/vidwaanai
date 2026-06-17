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

### Verse 1 (Vaivtpuran 543.17134)
- **Original**: धामको चला गया। उस समय श्रृगालके शरीरसे कीौजिये। नाथ! भवसागर बड़ा भयंकर है और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17135)
- **Original**: सात ताड़-जितनी लंबी एक महान्‌ ज्योति विषय-विषसे भी अधिक दारुण हैं; अतः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17136)
- **Original**: निकली और वह ब्रह्माजी तथा लक्ष्मीजीके द्वारा मेरी स्वकर्मजनित माया-मोहरूपी साँकलको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17137)
- **Original**: पूजित श्रीकृष्णेक चरणकमलोंमें प्रणाम करके छिन्न-भिन्न कर दीजिये। आप कर्मोंके ईश्वर, [चली गयी। ब्रह्माके भी विधाता, शुभ फलोंके दाता, समस्त तब अपने साथियोंके सहित श्रीमान्‌ कृष्ण सम्पत्तियोंके प्रदाता, प्राक्तन कर्मोके कारण और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17138)
- **Original**: इस अद्भुत चरित्रकों देखकर प्रफुल्लमुख हो उनके खण्डनमें समर्थ हैं। मैं अपने इस द्वारकाकी ओर चल दिये। द्वारका पहुँचकर पाझ्ञभौतिक प्राकृत नश्वर देहका त्याग करके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17139)
- **Original**: उन्होंने पहले माता-पिताको प्रणाम किया। आपके ही बैकुण्ठके सातवें द्वारपर जाऊँगा; तदनन्तर रुक्मिणीके महलमें जाकर पुष्पशय्यापर क्योंकि वहीं मेरा घर है।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17140)
- **Original**: शयन किया। इस प्रकारका मित्रका स्तवन और अमृतोपम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17141)
- **Original**: (अध्याय 121) +3+“>-+कस कर ए>पत
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17142)
- **Original**: * अश्रीकृष्णजन्मखण्ड + 759 ####%##%&##%#%# ####&##########
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17143)
- **Original**: &#&#8#&##&##&######&###8##&##%# 6 ###&#####&###&######%#####%&#&##%#% गणेशके अग्रपूज्यत्व-वर्णनके प्रसड़में राधाद्वारा गणेशकी अग्रपूजाका कथन नारदजीने पूछा--मुने ! पुराणोंमें जो गणेश-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17144)
- **Original**: प्रधान नागोंके साथ शेषनाग भी तुरंत ही वहाँ आ पूजनका दुर्लभ आख्यान वर्णित है, उसे मैंने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17145)
- **Original**: पहुँचे।फिर सभी देवता, मनु और मुनिगण भी वहाँ सामान्यतया ब्रह्माके मुखसे संक्षेपमें सुना है। अब
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17146)
- **Original**: आये। सभी नरेश प्रसन्नमनसे गणेशकी पूजा आपसे समस्त पूजनीयोंमें प्रधान गणपतिकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17147)
- **Original**: करनेके लिये वहाँ उपस्थित हुए। द्वारकावासियोंके महिमा विस्तारपूर्वक सुननेकी मेरी अभिलाषा है;
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17148)
- **Original**: साथ भगवान्‌ श्रीकृष्णका भी वहाँ शुभागमन हुआ क्योंकि आप योगीन्द्रोंक गुरुके भी गुरु हैं।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17149)
- **Original**: तथा गोकुलवासियोंके साथ नन्‍्द भी पधारे। पूर्वकालमें स्वर्गवासियोंने सिद्धाश्रममें रधा-माधवकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17150)
- **Original**: तदनन्तर सुरसिका, रासेश्वरी और श्रीकृष्णके प्राणोंकी महापूजा की थी; उसी राधाने सौ वर्षके बीतनेपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17151)
- **Original**: अधिदेवता सुन्दरी राधा भी सौ वर्ष व्यतीत हो जब श्रीदामाका शाप निवृत्त हुआ; तब ब्रह्मा,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17152)
- **Original**: जानेपर गोलोकवासिनी गोपी-सख्तियोंके साथ पधारी। विष्णु और शिव आदि सुरेन्‍्द्रों, नागराज शेष और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17153)
- **Original**: वहाँ सुन्दर दाँतोंवाली राधाने भलीभाँति स्नान अन्यान्य बड़े-बड़े नागों, भूतलपर बहुत-से
- **Translation**: 

---

