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

### Verse 1 (Vishnu Puran 0.9221)
- **Original**: गोबर और राख-भरे शरोरसे इधर-उधर घूमते हुए उन बाल्कॉको यश्योदा और ग्रेडिणी ग्रेक नहीं सकती थीं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9222)
- **Original**: कभी से गौओंके घोषमें स्ेलते और कभी चछड़ोंके मध्यमें चले जाते तथा कभी उसी दिन जन्मे हुए बछड़ोंकी पूछ पकड़कर खींचने लगते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9223)
- **Original**: एक दिन जब यज्ञोदा, सदा एक ही स्थानपर साथ- साथ खेलनेवाले उन दोनों अत्यन्त चश्चल बालकोंकों न रोक सकी तो उसने अनायास ही सब कर्म करनेवाऊे कुष्णको रस्सीसे कटिभागमें कसकर ऊखलमें बाँध दिया और रोषपूर्वक इस प्रकार कहने लगी--
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9224)
- **Original**: “अरे चच्धछ ! अब तुझमें सामर्थ्य हो तो चला जा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9225)
- **Original**: " ऐसा कहकर कुूट्म्बिनी यशोदा अपने घरके घन्धेमें लगा गयी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9226)
- **Original**: उसके गृहकार्यमें व्यग्र हो जानेपर कमलनयन कृष्ण ऊस्बजको खींचते खींचते बमल्र्जुनके. बीचमें गये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9227)
- **Original**: और उन दोनों वृक्षोंके बीचमें तिरत्ली पड़ी हुई ऊक्कलको खींचते हुए उन्होंने ऊँची शाखाओंवाले यमल्ार्जुन-बुक्षकों उखाड़ डाला
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9228)
- **Original**: तब उनके उखड़नेका कट-कट दाब्द सुनकर वहाँ व्रजवासील्प्रेग दौड़ आये और उन दोनों महावृक्षोको तथा उनके बीचमें कमरमें रस्सीसे कसकर बैंधे हुए बारूकको ननहें-नलें अल्प दाँतोंकी श्लेत किरणोंसे शुभ हास करते देस्ता। तभीसे रस्सीसे बैंधघनेके कारण उनका नाम दामोदर गड़ा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9229)
- **Original**: 18--20
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9230)
- **Original**: तब नन्दगोप आदि समस्त बुद्ध गोपोनि महान्‌ उत्पातोंके कारण अत्पन्त भयभीत होकर आपसमें यह सलाह कौ---
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9231)
- **Original**: 'अब इस स्थानपर रहनेका हमारा कोई प्रयोजन नहीं है, हमें किसी और महाबनको चलना चाहिये । क्योंकि यहाँ नाइके कारणस्वरूप, पूतना-यध, छकड़ेका स्जेट जाना तथा आँधी आदि किसी दोषके बिना ही वृक्षोका गिर पड़ना इत्यादि बहुत-से उत्पात दिखायी देने लगे हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9232)
- **Original**: अतः जबतक कोई भूमिसम्बन्धी महान्‌ उत्पात ब्रजको नष्ट न करे तबतक शीघ्र ही हमस्कोग इस स्थानसे त॒न्दावनकों चल दें
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9233)
- **Original**: इस प्रकार वे समस्त ब्रजबासी चलनेक्ा विचारकर अपने-अपने कुटुम्बके लछोगोंसे कहने लगे--' शीघ्र
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9234)
- **Original**: आ 6 ] तत: क्षणेन प्रययु: झकटेगोथिनैस्तथा । यूथज्ञो वत्सपालाश्न कालयन्तो व्रजोकस:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9235)
- **Original**: 26 द्रव्यावयवनिर्द्धूत॑ क्षणमात्रेण तत्तथा । काकभाससमाकीर्ण त्रजस्थानमभूदूद्विज
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9236)
- **Original**: 27 वृन्दावन भगवता कृष्णेनाह्लिपष्टकर्मणा । शुभेन मनसा ध्याते गवाँ सिद्धिमभभीप्सता
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9237)
- **Original**: 28 ततस्तत्रातिरूक्षेदपि घर्मकाले ब्विजोत्तम । प्रावृद्काल इवोद्धूत नवशष्पं समन्ततः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9238)
- **Original**: 29 स समावासित: सर्वों ब्रजो वृन्दावने ततः । चजकटीवाटपर्यन्तश्नद्धार््धाकारसंस्थिति:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9239)
- **Original**: 30 वत्सपालौ चर संवृत्ती रामदामोदरौ ततः । एकस्थानस्थितौ गोष्ठे चेरतुर्बाललीलया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9240)
- **Original**: 31 बहिंपत्रकृतापाड॑. वन्यपुष्पावतंसकौ । गोपवेणुकृतातोदयपत्रवाद्यकृतस्वनौ
- **Translation**: 

---

