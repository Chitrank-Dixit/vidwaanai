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

### Verse 1 (Vaivtpuran 0.61)
- **Original**: किस सेतुका निर्माण (मर्यादाकी स्थापना) आख्यान हो, जीवोंके कर्मविषपाकका प्रतिपादन
- **Translation**: 

---

### Verse 2 (Vaivtpuran 0.62)
- **Original**: करके वे भगवान्‌ पुनः गोलोककों पधारे? इन तथा नरकोंका भी वर्णन हो, जहाँ कर्मबन्धनका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 0.63)
- **Original**: सबसे तथा अन्य उपाख्यानोंसे परिपूर्ण जो खण्डन तथा उन कर्मोसे छूटनेके उपायका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 0.64)
- **Original**: श्रुतिदुर्लभ पुराण है, उसका सम्यक्‌ ज्ञान निरूपण हो, उसे सुनाइये। जिन जीवधारियोंको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 0.65)
- **Original**: मुनियोंके लिये भी दुर्लभ है। वह मनको निर्मल जहाँ जो-जो शुभ या अशुभ स्थान प्राप्त होता
- **Translation**: 

---

### Verse 6 (Vaivtpuran 0.66)
- **Original**: बनानेका उत्तम साधन है। अपने ज्ञानके अनुसार हो, उन्हें जिस कर्मसे जिन-जिन योगनियोंमें जन्म
- **Translation**: 

---

### Verse 7 (Vaivtpuran 0.67)
- **Original**: मैंने जो भी शुभाशुभ बात पूछी है या नहीं लेना पड़ता हो, इस लोकमें देहधारियोंको जिस
- **Translation**: 

---

### Verse 8 (Vaivtpuran 0.68)
- **Original**: पूछी है, उसके समाधानसे युक्त जो पुराण कर्मसे जो-जो रोग होता हो तथा जिस कर्मके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 0.69)
- **Original**: तत्काल बैराग्य उत्पन्न करनेवाला हो, मेरे समक्ष अनुष्ठानसे उन रोगोंसे छुटकारा मिलता हो, उन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 0.70)
- **Original**: उसीकी कथा कहिये। जो शिष्यके पूछे अथवा सबका प्रतिपादन कीजिये। बिना पूछे हुए विषयकी भी व्याख्या करता है सूतनन्दन! जिस पुराणमें मनसा, तुलसी,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 0.71)
- **Original**: तथा योग्य और अयोग्यके प्रति भी समभाव काली, गड्रा और वसुन्धरा पृथ्वी-इन सबका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 0.72)
- **Original**: रखता है, वही सत्पुरुषोंमें श्रेष्ठ सदगुरु है। तथा अन्य देवियोंका भी मज्नलमय आख्यान हो, सौति बोले--मुने ! आपके चरणारविन्दोंका शालग्राम-शिलाओं तथा दानके महत्त्वका निरूपण
- **Translation**: 

---

### Verse 13 (Vaivtpuran 0.73)
- **Original**: दर्शन मिल जानेसे मेरे लिये सब कुशल-ही- हो अथवा जहाँ धर्माधर्मके स्वरूपका अपूर्ब
- **Translation**: 

---

### Verse 14 (Vaivtpuran 0.74)
- **Original**: कुशल है। इस समय मैं सिद्धक्षेत्रसे आ रहा विवेचन उपलब्ध होता हो, उसका वर्णन
- **Translation**: 

---

### Verse 15 (Vaivtpuran 0.75)
- **Original**: हूँ और नारायणाश्रमको जाता हूँ। यहाँ ब्राह्मणसमूहकों
- **Translation**: 

---

### Verse 16 (Vaivtpuran 0.76)
- **Original**: है * संक्षिप्त ब्रह्मवैवर्तपुराण « 4444 42 4 2964 6 29 6 6 2 3 8 6 2 8
- **Translation**: 

---

### Verse 17 (Vaivtpuran 0.77)
- **Original**: 0 404/0/4440424]444]444646, नल ानम तलब म कमाल जल ल अर अमल लर जम नम कम. अप मल न 3
- **Translation**: 

---

### Verse 18 (Vaivtpuran 0.78)
- **Original**: लिये यह साक्षात्‌ कल्पवृक्ष-स्वरूप है। इसके कप
- **Translation**: 

---

### Verse 19 (Vaivtpuran 0.79)
- **Original**: ब्रहाखण्डमें सर्ववीजस्वरूप उस पर्रह्म परमात्माका 7:+00)
- **Translation**: 

---

### Verse 20 (Vaivtpuran 0.80)
- **Original**: निरूपण है जिसका योगी, संत और वैष्णव ध्यान
- **Translation**: 

---

