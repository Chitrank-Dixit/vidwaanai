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

### Verse 1 (Vishnu Puran 0.1141)
- **Original**: हे द्विज ! बहाजीद्वारा रचे गये जिन अनप्रिक अग्निक्वात्ता और साम्रिक बर्हिषद्‌ आदि पितरोंके विष्यमें तुमसे कहा था । उनके द्वारा स्वधाने सेना और घारिणी नामक दो कन्याएँ उत्पन्न कीं। वे दोनों ही उत्तम ज्ञानसे सम्पन्न और सभो-णुणोंसे युक्त ब्रह्मवादिनी तथा योगिनी थीं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1142)
- **Original**: 18---20
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1143)
- **Original**: इस प्रकार यह दक्षकन्याओकी बँडापरम्पराका वर्णन किया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1144)
- **Original**: जो छ्टेई श्रद्धापूर्वक इसका स्मरण करता है बह निःसन्तान नहीं रहता
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1145)
- **Original**: । 0, और स0-_-_>»»>___ इति श्रीविष्णुपुराणे प्रथमेंडशे दश्ामोड्थ्यायः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1146)
- **Original**: -छऋऋन है अन्‍फलचा ग्यारह॒वाँ अध्याय धुक्‍का वनगमन और मरीनि आदि ऋषियोंसे भेंट अ्रीपराज्ार उवाच प्रियब्रतोत्तानपादौ मनो: स्वायंभुवस्य तु। दी पुत्रो तु महावीयों धर्मज्ो कथितौ तव
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1147)
- **Original**: 1 तयोरुत्तानपादस्प सुरुच्यामुत्तम: सुतः । अभीष्टायामभूड्हान्पितुरत्यन्तवल्लभ:.
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1148)
- **Original**: 2 सुनीतिरनाम या राज्ञस्तस्पासीन्पहिषी द्विज । श्रीपराइरजी खोक्ले--हे मैप्रेय! यैने तुसं स्वायम्भुवमनुके प्रियत्रत एजं उत्तानपाद नामक दो महायलवान्‌ और भधर्मज्ञ पुष्र बतलाये थे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1149)
- **Original**: हे अत्मन्‌ ! उनमेंसे उत्तानपादको प्रेयसी पत्नी सुरुचिसे पिताका अल्यन्त स्णडछा उत्तम नामक पुत्र हुआ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1150)
- **Original**: हे ट्रिज ! उस राजाकी जो सुनीति नामक राजमंहिंषी थी उसमें उसका विशेष श्रेम न था। उसका पुत्र ध्रुव स नातिप्रीतिमांस्तस्यामभूदयस्या धुव:ः सुत:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1151)
- **Original**: अ* 11 ] अधम अंधा डर राजासनस्थितस्पाडूं. पितुर्श्रातरमाभ्रितम्‌ । एक दिन राजसिंहासनपर बैठे हुए पिताको गोदमें दृष्लोत्तम॑ धुवश्षक्रे तमारोदुं मनोरथम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1152)
- **Original**: अपने भाई उत्तमको बैठा देख घुक्‍्की इच्छा भी गोदमें प्रत्यक्ष भूषतिस्तस्या: सुरुच्या नाभ्यनन्दत । प्रणयेनागत पुम्रमुत्सड्रारोहणोत्सुकम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1153)
- **Original**: 5 सपत्रीतनयं दृष्ठा तमड्जारोहणोत्सुकम्‌ । स्वपुत्र तन तथारूढं सुरुचिर्वाक्यपत्रवीत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1154)
- **Original**: 6 क्रियते कि वृथा वत्स महानेष मनोरथ: । अन्यख््रीगर्भजातेन ह्वासम्भूय. ममोदरे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1155)
- **Original**: 7 उत्तमोत्तममप्राप्यमविवेको हि. वाउछसि । सत्य सुतस्त्वमप्यस्य किन्तु न स्व मया धृत:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1156)
- **Original**: 8 एतद्राजासन॑ सर्वभूभृत्संश्रयकेतनम्‌ । योग्यं ममैक पुत्रस्य किमात्मा क्लिह्यते त्वया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1157)
- **Original**: 9 उच्चैर्मनोरथस्तेडय॑मत्युत्रस्येव कि बृथा । सुनीत्यामात्मनो जन्प कि त्वया नावगम्यते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1158)
- **Original**: 10 अऔपराशर उवाच उत्सृज्य पितरं बालस्तच्छुत्वा मातृभाषितम्‌ । जगाम कुपितो मातुर्निजाया द्विज मन्दिरम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1159)
- **Original**: 19 ते दृष्ठ्ठा कुपितं पुत्रमीषत्मस्फुरिताधरम्‌। सुनीतिरद्भुमारोप्य मैन्नेयेदमभाषत
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1160)
- **Original**: 12 बत्स कः कोपहेतुस्ते कश्न त्वां नाभिनन्दति । को5वजानाति पितर॑ वत्स यस्तेउपराध्यति
- **Translation**: 

---

