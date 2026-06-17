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

### Verse 1 (Bramha 0.5761)
- **Original**: है तो भी वे लोक-कल्याणके लिये ही मानवरूपमें हो गयी, उस समय देवताओंके भी देवता जगत्पति
- **Translation**: 

---

### Verse 2 (Bramha 0.5762)
- **Original**: प्रकट हुए थे। ““*#स्येस्चे25.0
- **Translation**: 

---

### Verse 3 (Bramha 0.5763)
- **Original**: * सक्षम ग्रह्मपुराण + भ्रगवान्‌के अवतारका उपक्रम व्यासजी कहते हैं--मुनिवरो! अब मैं संक्षेपसे
- **Translation**: 

---

### Verse 4 (Bramha 0.5764)
- **Original**: श्रोहरिके अवतारका वर्णन करता हूँ, सुनो। भगवान्‌ इस पृथ्वीका भार उतारनेकी इच्छासे अवतार लेते हैं। जब-जब अधर्मको वृद्धि होती है और धर्मका हास होने लगता है, तब-तब भगवान्‌ जनार्दन 22 अपने स्वरूपके दो भाग करके यहाँ अबतीर्ण
- **Translation**: 

---

### Verse 5 (Bramha 0.5765)
- **Original**: £ होते हैं। साधु पुरुषोंकी रक्षा, धर्मकी स्थापना,
- **Translation**: 

---

### Verse 6 (Bramha 0.5766)
- **Original**: ँ दुष्टों तथा अन्य देव-द्रोहियोंका दमन और प्रजावर्गका पालन करनेके लिये वे प्रत्येक युगर्में अवतार
- **Translation**: 

---

### Verse 7 (Bramha 0.5767)
- **Original**: [** धारण करते हैं। पहलेकी बात है, यह पृथ्वी
- **Translation**: 

---

### Verse 8 (Bramha 0.5768)
- **Original**: अत्यन्त भारसे पीड़ित हो मेरुपर्वतपर देवताओंके समाजमें गयी और ब्रह्मा आदि सब देवताओंको 58 प्रणाम करके खेद एवं करुणामिश्रित बाणामें
- **Translation**: 

---

### Verse 9 (Bramha 0.5769)
- **Original**: (3 अपना सब हाल सुनाने लगी--'सुवर्णके गुरु 52.3 80 अग्रि, गौओंके गुरु सूर्य तथा मेरे गुरु सम्पूर्ण
- **Translation**: 

---

### Verse 10 (Bramha 0.5770)
- **Original**: पृथ्वीका यह बचन सुनकर सम्पूर्ण देवताओंने लोकोंके वन्दनीय भगवान्‌ नारायण हैं। इस समय
- **Translation**: 

---

### Verse 11 (Bramha 0.5771)
- **Original**: उसका भार उतारनेके लिये ब्रह्माजीको प्रेरित ये कालनेमि आदि दैत्य मर्त्यलोकमें जन्म लेकर
- **Translation**: 

---

### Verse 12 (Bramha 0.5772)
- **Original**: किया। तब ब्रह्माजी बोले--'देवताओ! पृथ्वी जो दिन-रात प्रजाको कष्ट देते रहते हैं। सर्वशक्तिमान्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.5773)
- **Original**: कुछ कहती है, वह सब ठीक है। वास्तवमें मैं, भगवान्‌ विष्णुने जिस कालनेमि नामक महान्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.5774)
- **Original**: महादेवजी और तुमलोग--सब भगवान्‌ नारायणके असुरका वध किया था, वही अब उप्रसेनकुमार
- **Translation**: 

---

### Verse 15 (Bramha 0.5775)
- **Original**: ही स्वरूप हैं। भगवान्‌की जो विभूतियाँ हैं, कंसके रूपमें उत्पन्न हुआ है। अरिष्ट, धेनुक,
- **Translation**: 

---

### Verse 16 (Bramha 0.5776)
- **Original**: उन्हींकी परस्पर न्यूनता और अधिकता बाध्य- केशी, प्रलम्ब, नरक, सुन्दासुर, अत्यन्त भयंकर
- **Translation**: 

---

### Verse 17 (Bramha 0.5777)
- **Original**: बाधकरूपसे रहा करती है। इसलिये आओ, बलिकुमार बाणासुर तथा और भी जो महापराक्रमी
- **Translation**: 

---

### Verse 18 (Bramha 0.5778)
- **Original**: हमलोग क्षीरसागरके उत्तम तटपर चलें और वहाँ दुरात्मा दैत्य राजाओंके घरमें उत्पन्न हुए हैं,
- **Translation**: 

---

### Verse 19 (Bramha 0.5779)
- **Original**: श्रीहरिकी आराधना करके यह सब वृत्तान्त उनसे उनको मैं गणना नहीं कर सकती । दिव्यमूर्तिधारी
- **Translation**: 

---

### Verse 20 (Bramha 0.5780)
- **Original**: निवेदन करें। वे सबके आत्मा हैं, सम्पूर्ण जगत्‌ देवताओ! इस समय मेरे ऊपर महाबलीं और
- **Translation**: 

---

