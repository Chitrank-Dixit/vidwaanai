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

### Verse 1 (Bramha 0.5141)
- **Original**: अपने बलसे उन्मत्त और एक-दूसरेसे लाग-डाँट विस्तार करनेवाले नहीं होते। एक ही कोई ऐसा
- **Translation**: 

---

### Verse 2 (Bramha 0.5142)
- **Original**: रखनेवाले थे। एक दिन वे दोनों भगवान्‌ सूर्यको पुत्र होता है, जो समूचे कुलको धारण करता
- **Translation**: 

---

### Verse 3 (Bramha 0.5143)
- **Original**: नमस्कार करनेके लिये आकाशमें गये। ज्यों हो है। जो कुलका आधारभूत, पिता-माताका प्रियकारक
- **Translation**: 

---

### Verse 4 (Bramha 0.5144)
- **Original**: सूर्यके समीप पहुँचे, दोनोंके पंख जल गये और और पूर्वजोंका उद्धार करनेवाला है, वही बास्तवमें
- **Translation**: 

---

### Verse 5 (Bramha 0.5145)
- **Original**: दोनों थककर पर्वतके शिखरपर गिर पड़े। दोनों पुत्र है; अन्य जितने हैं, वे रोग हैं। हर्षण! तुमने
- **Translation**: 

---

### Verse 6 (Bramha 0.5146)
- **Original**: भाइयॉको निश्चेष्ट एवं अचेत होकर गिरा देख मेरे मनके अनुकूल बात कही है। यह तुम्हारे नाना
- **Translation**: 

---

### Verse 7 (Bramha 0.5147)
- **Original**: अरुण उनके दुःखसे दुःखी हो गये और भगवान्‌ भगवान्‌ सूर्यकों भी पसंद आयेगी। अत: तुम
- **Translation**: 

---

### Verse 8 (Bramha 0.5148)
- **Original**: सूर्यससे बोले-'भगवन्‌! ये दोनों पक्षी पृथ्वीपर गौतमी-तटपर जाओ और वहाँ स्नान करके
- **Translation**: 

---

### Verse 9 (Bramha 0.5149)
- **Original**: गिर पड़े हैं। इन्हें आश्वासन दें, जिससे इनकी मनको वशमें रखते हुए प्रसन्नचित्तसे जगदयोनि
- **Translation**: 

---

### Verse 10 (Bramha 0.5150)
- **Original**: मृत्यु न हो।! “तथास्तु” कहकर सूर्यने उनको शान्तस्वरूप भगवान्‌ विष्णुकी स्तुति करो। वे
- **Translation**: 

---

### Verse 11 (Bramha 0.5151)
- **Original**: जीवित कर दिया। गरुड़ भी उनको अबस्था >- :डसस सऊस कसअइ्ंनक्न--स्‍लटेी-घ ततघतघत_+++_+_______नलल्फ्ेफं-न्-_्तन्न्‍>न्‍त]ौ”्झ्््- उखालजजज् आंत चअआओ- * ने मानयन्ति ये शास्त्र ताचारं न बहुश्ुतान्‌ । बिहितातिक्रमं कुर्युयें ते नरकंगामित्र:
- **Translation**: 

---

### Verse 12 (Bramha 0.5152)
- **Original**: [44] सं0 ब्र0 पु0--9 (165। 36)
- **Translation**: 

---

### Verse 13 (Bramha 0.5153)
- **Original**: 250 * संक्षिप्त ब्रह्मपुरुण + सुनकर भगवान्‌ विष्णुके साथ वहाँ आये और
- **Translation**: 

---

### Verse 14 (Bramha 0.5154)
- **Original**: करके गोदावरीके दक्षिण किनारेकी भूमिपर विचरती उन्हें सान्त्वना देकर सुख पहुँचाया। तदनन्तर सब
- **Translation**: 

---

### Verse 15 (Bramha 0.5155)
- **Original**: रहती थे। उसके शरीरमें बुढ़ापा आ गया था। एक लोग अपने संतापका निवारण करनेके लिये
- **Translation**: 

---

### Verse 16 (Bramha 0.5156)
- **Original**: दिन उस भयानक राक्षसीने ब्राह्मणसे कहा--' विप्रवर ! गड़गतटपर गये। जटायु, अरुण, सम्पाति, गरुड़,
- **Translation**: 

---

### Verse 17 (Bramha 0.5157)
- **Original**: ये गद्जाजी हैं। तुम अन्य ब्राह्मणोंके साथ मिलकर सूर्य तथा भगवान्‌ विष्णु-सबने उस प्रचुर पुण्यदायक
- **Translation**: 

---

### Verse 18 (Bramha 0.5158)
- **Original**: यहाँ संध्योपासन करो। जो ब्राह्मण समयपर तीर्थमें प्रवेश किया। तबसे वह तीर्थ पतत्रितीर्थक
- **Translation**: 

---

### Verse 19 (Bramha 0.5159)
- **Original**: [+ नामसे विख्यात हुआ। वह विषका नाशक तथा
- **Translation**: 

---

### Verse 20 (Bramha 0.5160)
- **Original**: डझिंड: सम्पूर्ण अभीष्ट वस्तुओंको देनेवाला है। साक्षात्‌
- **Translation**: 

---

