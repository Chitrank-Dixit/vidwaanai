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

### Verse 1 (Bramha 0.6221)
- **Original**: उन्हें साथ ले अपने भवनमें चले गये। परस्पर प्राप्त करते हैं तथा अश्विनीकुमार, रुद्र, इन्द्र और
- **Translation**: 

---

### Verse 2 (Bramha 0.6222)
- **Original**: प्रणाम आदिके बाद अक्रूरने दोनों भाइयोंके साथ वसु आदि देवता प्रसन्न होकर उन्हें उत्तम बर देते
- **Translation**: 

---

### Verse 3 (Bramha 0.6223)
- **Original**: बैठकर भोजन किया और यथायोग्य उनसे सब हैं। इन्हीं भगवानने दैत्यराजकौ सेनाका विनाश
- **Translation**: 

---

### Verse 4 (Bramha 0.6224)
- **Original**: बातें निवेदन कीं। दुरात्मा दानव कंसने बसुदेव *स ददर्श त़दा तत्र कृष्णमादोहने गवाम्‌। बत्समध्यगतं फुल्लनीलोत्पलदलच्छविम्‌
- **Translation**: 

---

### Verse 5 (Bramha 0.6225)
- **Original**: प्रफुल्लपद्मपत्राक्षं श्रीव॒त्साड़रि तवक्षसम्‌
- **Translation**: 

---

### Verse 6 (Bramha 0.6226)
- **Original**: प्रलम्यवाहुमायामतुज़ोर:स्थलमु्नसम्‌
- **Translation**: 

---

### Verse 7 (Bramha 0.6227)
- **Original**: सिलासस्मिताधार॑ बिभ्राण॑ मुखपड्ू जम्‌
- **Translation**: 

---

### Verse 8 (Bramha 0.6228)
- **Original**: तुड्गरक्तनखं पद्धघां धरण्यां सुप्रतिष्ितम्‌
- **Translation**: 

---

### Verse 9 (Bramha 0.6229)
- **Original**: बिध्राणं वाससी पीते बन्‍्यपुष्पविभूषितम्‌
- **Translation**: 

---

### Verse 10 (Bramha 0.6230)
- **Original**: साद्रनीललताहस्त॑ सिताम्भौजावतंसकम्‌
- **Translation**: 

---

### Verse 11 (Bramha 0.6231)
- **Original**: इंसेन्दुकुन्दघवल॑ नोलाम्बरघरं. द्विजाः
- **Translation**: 

---

### Verse 12 (Bramha 0.6232)
- **Original**: तस्वानु बलभद्र च ददर्श यदुनन्दनम्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.6233)
- **Original**: ग्रांशमुन्ुत़्याई च. विकाशिमुखपद्भजम्‌ । मेघमालापरिवृत कैलासाट्रिमिवापरम्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.6234)
- **Original**: (191। 19--24)
- **Translation**: 

---

### Verse 15 (Bramha 0.6235)
- **Original**: » अक्ुरका नन्दगाँवमें जाता, श्रीराम-कृष्णकी मधुरायात्रा «» 3061 और देवकीको जिस प्रकार धमकाया था, उग्रसेनके
- **Translation**: 

---

### Verse 16 (Bramha 0.6236)
- **Original**: मथुरा जाते हैं। क्रूर अक्रूरने उन्हें चकमा दिया है। प्रति जैसा उसका बर्ताव था और जिस उद्देश्यसे
- **Translation**: 

---

### Verse 17 (Bramha 0.6237)
- **Original**: क्या इस निर्दयीको प्रेमीजनोंकी मानसिक बेदनाका कंसने उन्हें व्रजमें भेजा था, वह सब विस्तारके
- **Translation**: 

---

### Verse 18 (Bramha 0.6238)
- **Original**: अनुभव नहीं है, जो यह हमारे नयनानन्द गोविन्दकों साथ कह सुनाया। सुनकर भगवान्‌ श्रीकृष्णने
- **Translation**: 

---

### Verse 19 (Bramha 0.6239)
- **Original**: अन्यत्र लिये जाता है? गोविन्द भी आज अत्यन्त कहा--'ये सब बातें मुझे ज्ञात हैं। इस विषयमें
- **Translation**: 

---

### Verse 20 (Bramha 0.6240)
- **Original**: निष्ठुर हो गये हैं। देखो न, बलरामजोके साथ जो उचित कर्तव्य है, उसे मैं करूँगा। आप
- **Translation**: 

---

