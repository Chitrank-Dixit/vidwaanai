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

### Verse 1 (Vaivtpuran 13.10442)
- **Original**: मनके समान तीज गतिसे चलनेवाली थीं। अतः भवभीत अच्युतको दिया था, उसी रूपमें वे इस
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10443)
- **Original**: आधे निमेषमें वहाँ जा पहुँचीं। उनकी वाणी समय दिखायी दिये। राधा व्यथित-हृदयसे लंबी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10444)
- **Original**: स्नरिग्ध एवं मधुर थी। आँखें लाल हो गयी थीं। साँस खींचकर इधर-उधर उस नव-तरुण श्रीकृष्णको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10445)
- **Original**: वे यशोदाजीकी गोदमें उस बालकको देनेके लिये देखने और दूँढ़ने लगीं। वे शोकसे पीड़ित और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10446)
- **Original**: उद्यत हो इस प्रकार बोलीं--' मैया ! ब्रजमें आपके विरहसे व्याकुल हो उठीं। उन्होंने कातरभावसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10447)
- **Original**: स्वामीने मुझे यह बालक घर पहुँचानेके लिये श्रीकृष्णके उद्देश्यससे यह दीनतापूर्ण बात कही-- [दिया था। भूखसे आतुर होकर रोते हुए इस “मायेश्व! आप अपनी इस दासीके प्रति ऐसी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10448)
- **Original**: स्थूलकाय शिशुको लेकर मैं रास्तेभर यातना भोग माया क्‍यों करते हैं ?' इतना कहकर राधा पृथ्वीपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10449)
- **Original**: रही हूँ। मेरा भीगा हुआ वस्त्र इस बच्चेके शरीरमें गिर पड़ीं और रोने लगीं। उधर बालकृष्ण भो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10450)
- **Original**: सट गया है। आकाश बादलोंसे घिरा हुआ है। वहीं रो रहे थे। इसी समय आकाशवाणी हुई--'राधे !
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10451)
- **Original**: अत्यन्त दुर्दिन हो रहा है, मार्गमें फिसलन हो तुम क्‍यों रोती हो? श्रीकृष्फे चरणकमलका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10452)
- **Original**: रही है। कौच-काच बढ़ गयी है। यशोदाजी! चिन्तन करो। जबतक रासमण्डलकी आयोजना
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10453)
- **Original**: अब मैं इस बालकका बोझ ढोनेमें असमर्थ हो नहीं होती, तबतक प्रतिदिन रातमें तुम यहाँ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10454)
- **Original**: गयी हूँ। भद्ने! इसे गोदमें ले लो और स्तन देकर आओगी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10455)
- **Original**: अपने घरमें अपनी छाया छोड़कर स्वयं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10456)
- **Original**: शान्त करो। मैंने बड़ी देरसे घर छोड़ रखा है; यहाँ उपस्थित हो तुम श्रीहरिके साथ नित्य अत: जाती हूँ। सती यशोदे! तुम सुखी मनोवाज्छित क्रीड़ा करोगी। अतः रोओ मत।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10457)
- **Original**: रहो।' ऐसा कह बालक देकर राधा अपने घरको शोक छोड़ो और अपने इन बालरूपधारो प्राणेश्वर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10458)
- **Original**: चली गयीं। यशोदाने बालकको घरमें ले जाकर मायापतिकों गोदमें लेकर घरकों जाओ।' चूमा और स्तन पिलाया। राधा अपने घरमें रहकर जब आकाशवाणीने सुन्दरी राधाको इस
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10459)
- **Original**: बाह्रूपसे गृहकर्ममें तत्पर दिखायी देती थीं; परंतु प्रकार आश्वासन दिया, तब उसकी बात सुनकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10460)
- **Original**: प्रतिदिन रातमें वहाँ वृन्दावनमें जाकर श्रीहरिके राधाने बालकको गोदमें उठा लिया और पूर्वोक्त [साथ क्रीड़ा करती थीं। वत्स नारद! इस प्रकार युष्पोद्यान, वन तथा उत्तम रत्ममण्डपको ओर पुनः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10461)
- **Original**: मैंने तुमसे शुभद, सुखद तथा मोक्षदायक पुण्यमय दृष्टिपात किया। इसके बाद राधा वृन्दावनसे तुरंत
- **Translation**: 

---

