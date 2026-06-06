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

### Verse 1 (Bramha 0.8661)
- **Original**: इस ज्ञानके समान दूसरा कोई ज्ञान नहीं है। इसके न कॉजिपे विययोँ तुमको संदेह नहीं करना चाहिये
- **Translation**: 

---

### Verse 2 (Bramha 0.8662)
- **Original**: सांछाशन जो तथ्य हो, उसका यथावत्‌ वर्णन की 4: 2303 क्‍>पके लक कह ओ-+0 400 आपके सिवा दूसरे किसीसे हम ऐसा प्रश्न 2-53 >.00ज- 7703 >> हम आपने जो प्रश्न
- **Translation**: 

---

### Verse 3 (Bramha 0.8663)
- **Original**: ब्रह्म आदि, मध्य और अन्तसे रहित, द्नन्द्रोंसे 40-आा भ। अप क अतीत, सनातन, कूटस्थ और नित्य है--ऐसा 8-0 जो हल 72
- **Translation**: 

---

### Verse 4 (Bramha 0.8664)
- **Original**: शान्तिपरायण विद्वान्‌ पुरुषोंका कथन है। इसीसे ही कठिन है। इसमें
- **Translation**: 

---

### Verse 5 (Bramha 0.8665)
- **Original**: कम 20 -क+30ल- 4 आज नकल नेत-+3- न: कपिलके
- **Translation**: 

---

### Verse 6 (Bramha 0.8666)
- **Original**: विकार होते हैं। गृढ़ तत्त्वोंकी व्याख्या करनेवाले &-+्. जुक साल भहा्कयोका महर्षियोंने शास्त्रोंमें ऐसा हो वर्णन किया है। मा देहधारियोंकी
- **Translation**: 

---

### Verse 7 (Bramha 0.8667)
- **Original**: सम्पूर्ण ब्राह्मण, देवता, वेद तथा सामवेत्ता पुरुष विचार उत्तम माना गया है। देह
- **Translation**: 

---

### Verse 8 (Bramha 0.8668)
- **Original**: हक 2205 ्युत, बोल आछ कह “% की पर जा जो प भी
- **Translation**: 

---

### Verse 9 (Bramha 0.8669)
- **Original**: परमेश्वरकी प्रार्थना करते और उनके गुणोंका क्योंकि ' 42727: 72: कुं: 3+064%4:.8.050 अर"
- **Translation**: 

---

### Verse 10 (Bramha 0.8670)
- **Original**: और योगमें तथा पुराणोंमें जो उत्तम ज्ञान देखा जड़मात्र हैं तथा महासागरमें उसके है बह «
- **Translation**: 

---

### Verse 11 (Bramha 0.8671)
- **Original**: अछलो जी कया टआई। भूमिकी भाँति नष्ट हो जाती हैं। विप्रवरो! जब गया बह/मि/ 4-30. .1 4 इन्द्रियोंके साथ देहधारी जीव सो जाता परी हक मा शय सोष जो कुछ 00. कलम 4444 ..3 भी ज्ञान श्रेष्ठ पुरुषोंके देखनेमें आया है, वह सब सर्वत्र बिचरता रहता है। वह यथायोग्य वस्तुऑको
- **Translation**: 

---

### Verse 12 (Bramha 0.8672)
- **Original**: हू 14 फेज 4 नूर क3- 3 श3क देखता, स्मरण करता, छूता और पहलेकी हो हद; यो बे शकप बप आदि फिर भी भाँति उन सबका अनुभव करता है। सम्पूर्ण
- **Translation**: 

---

### Verse 13 (Bramha 0.8673)
- **Original**: का हमले ला सका बाप पक सास कक 94030 कॉम ब्त्‌ वर्णन किया गया है। सांख्यज्ञानों सदा मारे हुए सर्पोंकी भाँति अपने-अपने गोलकोंमें। यथाबत्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.8674)
- **Original**: ड16 * संक्षितत सहापुराण * सुखपूर्वक कल्याणमय भ्रह्मको प्राप्त होते हैं। उस
- **Translation**: 

---

### Verse 15 (Bramha 0.8675)
- **Original**: भगवान्‌ नारायण ही पूर्णरूपसे धारण करते हैं। ज्ञानकों धारण करके भी मनुष्य कृतार्थ हो जाते
- **Translation**: 

---

### Verse 16 (Bramha 0.8676)
- **Original**: मुनिवरो! यह मैंने तुमसे परम तत्त्वका वर्णन किया। हैं। सांख्यका ज्ञान अत्यन्त विशाल और परम
- **Translation**: 

---

### Verse 17 (Bramha 0.8677)
- **Original**: यह सम्पूर्ण पुशतन विश्व भगवान्‌ नारायणसे ही प्राचीन है। यह महासागरके समान अगाध, निर्मल
- **Translation**: 

---

### Verse 18 (Bramha 0.8678)
- **Original**: प्रकट हुआ है। वे ही सृष्टिके समय संसारकी सृष्टि और उदार भावोंसे पूर्ण है। इस अप्रमेय ज्ञानको
- **Translation**: 

---

### Verse 19 (Bramha 0.8679)
- **Original**: और संहारकालमें उसका संहार करते हैं। 8 “अग्पि सर 8->> क्षर-अक्षर-तत्त्वके विषयमें राजा करालजनक और वसिष्ठका संवाद मुनियोंने पूछा--महामुने! बह अक्षर-तत्त्व
- **Translation**: 

---

### Verse 20 (Bramha 0.8680)
- **Original**: चतुर्युग होता है। एक हजार चतुर्युगको ब्रह्माका क्या है, जिसको प्राप्त कर लेनेपर जीव पुन: इस
- **Translation**: 

---

