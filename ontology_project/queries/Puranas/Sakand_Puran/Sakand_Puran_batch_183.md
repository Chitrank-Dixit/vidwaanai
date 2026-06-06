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

### Verse 1 (Sakand Puran 9.10041)
- **Original**: सन्तोषासृततृप्तानां यत्सुत्ं शझान्तचेतसास्‌ । कुशस्तद्नठुण्पानामितरचेत शव धायताम्‌
- **Translation**: 

---

### Verse 2 (Sakand Puran 9.10042)
- **Original**: असन्तोर पर दुःछ॑सम्वो्ष परम सुख़म्‌ । सुस्तमा्थी पुस्पस्तस्माव्‌ सन्तुषटः सतत भक्त
- **Translation**: 

---

### Verse 3 (Sakand Puran 9.10043)
- **Original**: ( रक0 पु0 नोॉ0 12
- **Translation**: 

---

### Verse 4 (Sakand Puran 9.10044)
- **Original**: 47-49 ) * या दुस्त्यजा दुर्मतिम्रियाँ न जोयंति जीवंत: । याउसौ प्रागास्तओं रोगत्ा
- **Translation**: 

---

### Verse 5 (Sakand Puran 9.10045)
- **Original**: न्‍्वुस्णां स्वजतः सुन
- **Translation**: 

---

### Verse 6 (Sakand Puran 9.10046)
- **Original**: ( स्क0 पु0 ला0 336
- **Translation**: 

---

### Verse 7 (Sakand Puran 9.10047)
- **Original**: 77 ) आचरण करते हैं; अपने ह्वितकी इब्छ। रखनेवाले विशपुरुषकों भी बैसा ही आचरण करना चाहिये । सूतजी कहते है--ऐसा कहकर वे सप्तर्पिणण उन सुबर्णगर्मित फर्लोकों यहीं छोड़कर अन्यत्र चछे गये । तत्पभ्रात्त्‌ उन्होंने चमत्कारपुरके क्षेत्रमें प्रवेश किया
- **Translation**: 

---

### Verse 8 (Sakand Puran 9.10048)
- **Original**: बह्ों पहुँचते ही उन्हें खला अपने खामने आया हुआ शुनोमुख नामक संन्यासी दिखायी दिया
- **Translation**: 

---

### Verse 9 (Sakand Puran 9.10049)
- **Original**: तत्र उसीके साथ वे किसी यनके मौतर गये
- **Translation**: 

---

### Verse 10 (Sakand Puran 9.10050)
- **Original**: थद्दों जानेपर उन सकने कमछोंसे मुशोमित एक सुन्दर सरोयर देखा
- **Translation**: 

---

### Verse 11 (Sakand Puran 9.10051)
- **Original**: तब्र भूखे पीढ़ित दोनेके कारण उन्होंने उस पोखरेसे बहुतेंरे सृणाऊ निकाछे और क़िनारेपर रखकर सख्थ्या-तर्पण आदि पुष्यकर्मोमें छय गये
- **Translation**: 

---

### Verse 12 (Sakand Puran 9.10052)
- **Original**: तदनन्तर वे सब छोग जलसे निकलकर एक दूसरेंसे मिले
- **Translation**: 

---

### Verse 13 (Sakand Puran 9.10053)
- **Original**: तय वहाँ उन सूजालौंकों न देखकर इस प्रकार कहने छगे
- **Translation**: 

---

### Verse 14 (Sakand Puran 9.10054)
- **Original**: ऋषि बोले--अहो ! हम भूखसे पीढ़ित हैं। इस दशामें भी किस निर्दवीनें हमारे समस्त सूणाल इस स्थानसे चुरा डिये हैं । शुनोमुखने कहा--जिसने इन मृणालोकों चुराया तथा निरल्तर सत्य बोछे । द्विजातियोंकों अमीए ही हैं
- **Translation**: 

---

### Verse 15 (Sakand Puran 9.10055)
- **Original**: अतः यह निश्चय हो गया कि इन सुलाकोंकी चोरी भीमानने दी की है । शुनोमुखने कहा--निश्रव मैंने दी आपलोगोंके मृणारू चुराये हैं । आप मुझे इल्द्र जानें
- **Translation**: 

---

### Verse 16 (Sakand Puran 9.10056)
- **Original**: दिजवरों ! आपमें छोभका अभाव देखकर मैं बहुत सन्तुष्ट हूँ । अतः आप मेरे साथ हीक्र स्वर्गलोकमें पधा
- **Translation**: 

---

### Verse 17 (Sakand Puran 9.10057)
- **Original**: ऋषि बोले--देवराज ! हम तो मोक्षमार्गके पथिक हैं। हमारे मनमें स्वर्गको लिप्सा नहीं है । अतः इस तीर्षमें मोक्षके लिये हम तपस्या करेंगे । जमदसिने कहा--सुरेश्वर ! इमने सृणालॉसे ही जीयन निर्वाह करते हुए समुद्रपर्यन्त समूची प्रप्यीकी परिक्मा कौ है। अब हमारे लाथ आपका जो समांगम दुआ है, इससे आपका ही कल्याण दो । आप यहाँसे स्वर्गलोककों पधारें । इन्द्र बोले--उत्तम जतका पाछन फरनेयाले मुनी्वरों ! मेरा दर्शन कभी व्यर्थ नहीं जाता
- **Translation**: 

---

### Verse 18 (Sakand Puran 9.10058)
- **Original**: इसलिये आपड़ोग अपनी कोई अभीष्ट वस्तु मुझते ग्रदण करें । ऋषियोंनि कद्दा--इन्‍्द्र ! इस प्रृथ्वीपर इमारे नामसे यह आश्रम विख्यात शो और यहाँ आनेवालछे मनुष्योफे सब
- **Translation**: 

---

### Verse 19 (Sakand Puran 9.10059)
- **Original**: <उट फातकोंका नाश करनेयाछां हो
- **Translation**: 

---

### Verse 20 (Sakand Puran 9.10060)
- **Original**: हम सदा यहीं तफ्स्याके लिये तबतक निवास करेंगे, जयतक कि इमें सनातन-मोक्षकी प्रासि नहीं हो जाती
- **Translation**: 

---

