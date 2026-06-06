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

### Verse 1 (Agni Puran 0.2421)
- **Original**: 6।1) 5. 35 यवो5सि यवयास्मदद्रपो यथयाराती:। (यजु0 5
- **Translation**: 

---

### Verse 2 (Agni Puran 0.2422)
- **Original**: इसी तरह पितामह आदिको भी दे। फिर सब
- **Translation**: 

---

### Verse 3 (Agni Puran 0.2423)
- **Original**: निम्नाड्धित मन्त्रका जप करे--'40 पृथिवी अर्घ्यका अवशेष पहले पात्रमें डाल दे अर्थात्‌
- **Translation**: 

---

### Verse 4 (Agni Puran 0.2424)
- **Original**: ते पात्र चीरपिधानं म्राह्मणस्य मुखे5मृते5मृतं जुहोमि प्रपितामहके अर्ध्यमें जो जल आदि हो, उसे
- **Translation**: 

---

### Verse 5 (Agni Puran 0.2425)
- **Original**: स्वाहा। इृद. विष्णुर्विचक्रमेि... त्रेधा पितामहके पात्रमें डाल दे। इसके बाद वह सब
- **Translation**: 

---

### Verse 6 (Agni Puran 0.2426)
- **Original**: निदधे पदम्‌ समूढमस्य पाशसुरे स्वाहा पिताके अर्ध्यपात्रमें रख दे। पिताके अर्ध्यपात्रको
- **Translation**: 

---

### Verse 7 (Agni Puran 0.2427)
- **Original**: कृष्ण इृव्यमिदं रक्ष मदीयम्‌।' (यजु0 5।15) पितामहके अर्घ्यपात्रके ऊपर रखे। फिर उन
- **Translation**: 

---

### Verse 8 (Agni Puran 0.2428)
- **Original**: ऐसा पढ़कर अन्तमें ब्राह्मणके अँगूठेका स्पर्श दोनोंको प्रपितामहके अर्घ्यपात्रके ऊपर रख दे।
- **Translation**: 

---

### Verse 9 (Agni Puran 0.2429)
- **Original**: कराबे। (देवपात्रोंपर “यवोउसि यवयास्मद- तत्पश्चात्‌ तीनोंकों पितांके आसनके बामभागमें
- **Translation**: 

---

### Verse 10 (Agni Puran 0.2430)
- **Original**: द्वेषो यवयाराती:।' इस मन्त्रसे जौ छींटे) और 'पितृभ्य: स्थानमसि।' ऐसा कहकर उलट दे।
- **Translation**: 

---

### Verse 11 (Agni Puran 0.2431)
- **Original**: पितरोंके पात्रोंपर “अपहता असुरा रक्षाश्सि तदनन्तर यहाँ देवताओं और पितरोंके लिये गन्ध,
- **Translation**: 

---

### Verse 12 (Agni Puran 0.2432)
- **Original**: वेदिषद: ।' इस मन्त्रसे तिल छींटकर संकल्पपूर्वक पुष्प, धूप, दीप तथा बस्त्र आदिका दान किया जाता है
- **Translation**: 

---

### Verse 13 (Agni Puran 0.2433)
- **Original**: 14--16
- **Translation**: 

---

### Verse 14 (Agni Puran 0.2434)
- **Original**: उसके बाद श्राद्धकर्ता पुरुष पात्रमेंसे घृतयुक्त अन्न निकालकर ब्राह्मणोंसे पूछे --/ मैं अग्निमें इस अन्नका हवन करूँगा।' ब्राह्मण आज्ञा दें-- “करो '। तब साग्निक पुरुष तो अग्निमें हबन करे अन्न अर्पण करे। तदनन्तर 'जुषघ्वम्‌।' ( आपलोग अन्न ग्रहण करें) ऐसा कहकर गायत्री-मन्त्र आदिका जप करे
- **Translation**: 

---

### Verse 15 (Agni Puran 0.2435)
- **Original**: 17--21
- **Translation**: 

---

### Verse 16 (Agni Puran 0.2436)
- **Original**: देवताभ्यः पितृभ्यश्च महायोगिभ्य एव च। नमः स्थधायै स्वाहाये नित्यमेव नमो नम:
- **Translation**: 

---

### Verse 17 (Agni Puran 0.2437)
- **Original**: *इस मन्त्रका भी जप करे। पितरोंको तृत और निरग्निक पुरुष पत्रित्रीयुक्त पितरके हाथ
- **Translation**: 

---

### Verse 18 (Agni Puran 0.2438)
- **Original**: जानकर पात्रमें अन्न बिखेरे। फिर एक-एक बार (अथवा जल)-में मच्नसे आहुति दे। पहली आहुति “अग्नये कव्यवाहनाय स्वाहा।' (यजु0 2।29) सबको जल दे। पूर्ववत्‌ सव्यभावसे गायत्री-जप करके “मधु बाता'' इस ऋचाका जप करे! कहकर दे। दूसरी आहुति “सोमाय पितृमते
- **Translation**: 

---

### Verse 19 (Agni Puran 0.2439)
- **Original**: इसके बाद ब्राह्मणोंसे पूछे --'आपलोग तृप्त हो स्वाहा।' (यजु0 2।29) इस मन्त्रसे दे। दूसरे
- **Translation**: 

---

### Verse 20 (Agni Puran 0.2440)
- **Original**: गये ?' ब्राह्मण कहें -हाँ, हम तृप्त हो गये।' विद्वानॉका मत है कि “यम' एवं “अड्विरा' के
- **Translation**: 

---

