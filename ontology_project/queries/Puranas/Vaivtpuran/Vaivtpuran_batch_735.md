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

### Verse 1 (Vaivtpuran 543.13014)
- **Original**: होती है, उन्हें बैसी ही सिद्धि प्राप्त होती है।' गयी थी। श्वेत चन्द्रमा ही मानो वृषभराज नन्‍्दी ऐसा कहकर योगीश्वर शंकरने व्याप्रचर्मपर बन गये थे और भूत आदि नर्तकॉंका काम
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13015)
- **Original**: योगासन लगाया और मुझ परब्रह्मरूप ज्योतिका करते थे। महेश्वरके स्वरूपमें तत्काल सब कुछ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13016)
- **Original**: तत्काल ध्यान आरम्भ कर दिया। तब देवी बदल गया। शिवका ऐसा रूप देख मेना बहुत
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13017)
- **Original**: पार्वतीने उनके दोनों चरण पखारकर चरणामृत- संतुष्ट हुई। कितनी रमणियाँ भगवान्‌ शंकरके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13018)
- **Original**: पान किया और अग्निशुद्ध वस्त्रसे भक्तिपूर्वक रूप-सौन्दर्यकों देखकर अत्यन्त मुग्ध हो गयीं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13019)
- **Original**: उन चरणोंका मार्जन किया। विश्वकर्मद्वारा निर्मित और नाना प्रकारकी अभिलाषाएँ करने लगों।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13020)
- **Original**: रमणीय रज्नसिंहासन उनकी सेवामें अर्पित किया। अहो! पार्वती बड़ी पुण्यवती है। भारतवर्षमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13021)
- **Original**: फिर कांस्यपात्रमें रखे हुए अपूर्व नैवेद्यका भोग इसीका जन्म स्पृहणीय है; क्योंकि ये शिव
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13022)
- **Original**: लगाया। तत्पश्चात्‌ उनके चरणोंमें गड्ाजलसे युक्त इसके स्वामी होनेवाले हैं। अर्ध्य दिया। इसके बाद मनोहर सुगन्धयुक्त चन्दन इस प्रकारकी बातें कितनी ही स्त्रियाँ कर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13023)
- **Original**: तथा कस्तूरी और कुंकुम भी सेवामें प्रस्तुत किये। रही थीं। शिवका दर्शन करके मेना सानन्द
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13024)
- **Original**: तदनन्तर हालाहल विषके चिहसे सुन्दर प्रतीत अपने घरकों लौट गयीं। शिवका पूजन करके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13025)
- **Original**: होनेवाले कण्ठमें मालतीकी माला पहनायी। उनके चरणोंमें मस्तक नवाकर शैलराज भी अपने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13026)
- **Original**: भक्ति-भावसे पूजा की। शिवकी प्रसन्नताके लिये घरको गये। गिरिराजने मेनाके साथ एकान्तमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13027)
- **Original**: उनपर पुष्पोंकी वृष्टि की। सुवर्णपात्रमें अमृत सलाह करके पार्वतीको उसकी मज्जल-कामनासे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13028)
- **Original**: और मधुर मधु दिया। सैकड़ों रलमय दीप शिवके समीप भेजा। पार्वतीका हृदय भगवान्‌.
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13029)
- **Original**: जलाये। सब ओर उत्तम धूपकी सुगन्ध फैलायी। शंकरमें अनुरक्त था। सखियोंके साथ मनोहर वेष
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13030)
- **Original**: त्रिभुवन-दुर्लभ वस्त्र, सोनेके तारोंका यज्ञोपवीत धारण करके हर्षपूर्वक वे शिवके निकट गयीं।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13031)
- **Original**: तथा पीनेके लिये सुगन्धित एवं शीतल जल वहाँ प्रसन्नमुख और नेत्रवाले शान्तस्वरूप शिवका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13032)
- **Original**: पार्वतीने अपने प्रियतमकी सेवामें प्रस्तुत दर्शन करके शिवाने सात बार परिक्रमा कौ और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13033)
- **Original**: किये। फिर रत्लसारेद्धनिर्मित अतिशय सुन्दर मुस्कराकर उन्हें प्रणाम किया। उस समय भगवान्‌
- **Translation**: 

---

