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

### Verse 1 (Bramha 0.3221)
- **Original**: + दशाश्यमेथिक और पैशाचतीर्थका माहात्म्य « श्ष्5 तीर्थका माहात्म्य सुनो। उसके श्रवणमात्रसे अश्वमेध- , ले मेरे पास आ पहुँचे और मुझसे भी उत्तम देश यज्ञके फलकी प्राप्ति होती है। विश्वकमकि पुत्र
- **Translation**: 

---

### Verse 2 (Bramha 0.3222)
- **Original**: आदिके विषयपें प्रश्त करने लगे। उस समय मैंने महाबली विश्वरूप हुए। विश्वरूपके प्रथम नामक
- **Translation**: 

---

### Verse 3 (Bramha 0.3223)
- **Original**: भौबन और कश्यपसे कहा--' राजेद्र ! तुम गोदावरीके पुत्र हुआ। उसके पुत्रका नाम भौवन हुआ।
- **Translation**: 

---

### Verse 4 (Bramha 0.3224)
- **Original**: तटपर जाओ। बही यज्ञके लिये पुण्यवान्‌ प्रदेश महाबाहु भौवन सार्वभौम राजा हुए। उनके पुरोहित
- **Translation**: 

---

### Verse 5 (Bramha 0.3225)
- **Original**: है। वेदोंके पारगामी विद्वान्‌ ये महर्षि कश्यप ही कश्यप थे, जो सब प्रकारके ज्ञानमें निपुण थे।
- **Translation**: 

---

### Verse 6 (Bramha 0.3226)
- **Original**: श्रेष्ठ गुरु हैं। इनकी कृपा और गौतमी गद्गभाके एक दिन महाबाहु भौवनने अपने पुरोहितसे
- **Translation**: 

---

### Verse 7 (Bramha 0.3227)
- **Original**: प्रसादसे एक ही अश्वमेघसे अथवा वहाँ स्नान पूछा--' मुने! मैं एक ही साथ दस अश्वमेध-यज्ञ
- **Translation**: 

---

### Verse 8 (Bramha 0.3228)
- **Original**: करनेमात्रसे तुम्हारे दस अश्वमेघ-यज्ञ सिद्ध हो करना चाहता हूँ। वह यज्ञ कहाँ करूँ?” कश्यपने
- **Translation**: 

---

### Verse 9 (Bramha 0.3229)
- **Original**: जायँगे।' यह सुनकर राजा भौवन कश्यपजीके प्रयागका नाम लिया और उन-उन स्थानॉपर यज्ञ
- **Translation**: 

---

### Verse 10 (Bramha 0.3230)
- **Original**: साथ गौतमीके तटपर आये और वहाँ अश्वमेध- करनेको बताया, जहाँ श्रेष्ठ द्विजोंने पूर्वकालमें
- **Translation**: 

---

### Verse 11 (Bramha 0.3231)
- **Original**: यज्ञकी दीक्षा ग्रहण की। बह महायज्ञ आरम्भ बड़े-बड़े यज्ञोंका अनुष्ठान किया था। राजाके
- **Translation**: 

---

### Verse 12 (Bramha 0.3232)
- **Original**: होकर जब पूर्ण हो गया, तब राजा इस पृथ्वीका यज्ञमें बहुत-से ऋषि ऋत्विज हुए। पुरोहितने एक
- **Translation**: 

---

### Verse 13 (Bramha 0.3233)
- **Original**: दान करनेको उद्यत हुए। उसी समय आकाशबाणी ही साथ दस अश्वमेध-यज्ञ आरम्भ किये, किंतु
- **Translation**: 

---

### Verse 14 (Bramha 0.3234)
- **Original**: हुई--“राजन्‌! तुमने पुरोहित कश्यपजीको पर्वत,बन उनमेंसे एक भी पूर्ण न हुआ। यह देखकर
- **Translation**: 

---

### Verse 15 (Bramha 0.3235)
- **Original**: और काननोंसहित पृथ्वी देनेकी कामना करके राजाको बड़ी चिन्ता हुई। उन्होंने प्रयाग छोड़कर
- **Translation**: 

---

### Verse 16 (Bramha 0.3236)
- **Original**: सब कुछ दान कर दिया। अब भूमिदानकी अन्य स्थानोंमें उन यज्ञॉका आरम्भ किया, किंतु
- **Translation**: 

---

### Verse 17 (Bramha 0.3237)
- **Original**: अभिलाषा छोड़कर अन्नदान करो। वह महान्‌ वहाँ भी विश्न-दोष आ पहुँचे। इस प्रकार अपने
- **Translation**: 

---

### Verse 18 (Bramha 0.3238)
- **Original**: फल देनेवाला है। तीनों लोकोमें अन्नदानके समान यज्ञोंको अपूर्ण देख राजाने पुरोहितसे कहा--' देश
- **Translation**: 

---

### Verse 19 (Bramha 0.3239)
- **Original**: दूसरा पुण्यकार्य नहीं है। विशेषत: गड्जाजीके और कालके दोषसे अथवा मेंरे और आपके दोषसे
- **Translation**: 

---

### Verse 20 (Bramha 0.3240)
- **Original**: तटपर श्रद्धाके साथ किये हुए अन्नदानकी महिमा हमारे दस अश्वमेध-यज्ञ पूर्ण नहीं हो पाते।' यों
- **Translation**: 

---

