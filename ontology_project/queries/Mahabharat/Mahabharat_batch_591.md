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

### Verse 1 (Mahabharat 0.5901)
- **Original**: करना बिडम्बनामात्र है। मेरा तो विश्वास है कि धर्मका ढोंग हुआ, वे एकान्तमें उनके पास जाकर ओोलीं--'राजन्‌ !
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5901)
- **Original**: करना बिडम्बनामात्र है। मेरा तो विश्वास है कि धर्मका ढोंग हुआ, वे एकान्तमें उनके पास जाकर ओोलीं--'राजन्‌ !
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5902)
- **Original**: रचानेबाले मधमुंडे अपनी जीविका चल्मानेके लिये:ही ऐसा आपको भिक्षुककी भाँति मुद्ठीभर भुना हुआ जौ खाकर
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5902)
- **Original**: रचानेबाले मधमुंडे अपनी जीविका चल्मानेके लिये:ही ऐसा आपको भिक्षुककी भाँति मुद्ठीभर भुना हुआ जौ खाकर
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5903)
- **Original**: करते हैं। जो हो, आप तो साथु-महात्माओंका पालन-पोषण रहना उचित नहीं है। आपकी यह प्रतिज्ञा और चेष्टा सब
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5903)
- **Original**: करते हैं। जो हो, आप तो साथु-महात्माओंका पालन-पोषण रहना उचित नहीं है। आपकी यह प्रतिज्ञा और चेष्टा सब
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5904)
- **Original**: करते हुए जितेख्रिय होकर पुण्यस्प्रेकॉंपर अधिकार प्राप्त राजधर्मके विरुद्ध है। यह महान्‌ राज्य छोड़कर यदि आप
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5904)
- **Original**: करते हुए जितेख्रिय होकर पुण्यस्प्रेकॉंपर अधिकार प्राप्त राजधर्मके विरुद्ध है। यह महान्‌ राज्य छोड़कर यदि आप
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5905)
- **Original**: कीजिये। जो प्रतिदिन गुरुके लिये समिथा ल्मता है-अथवा थोड़े-से अन्नमें संतोष मानते हैं तो इतने-से अतिथि, देवता,
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5905)
- **Original**: कीजिये। जो प्रतिदिन गुरुके लिये समिथा ल्मता है-अथवा थोड़े-से अन्नमें संतोष मानते हैं तो इतने-से अतिथि, देवता,
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5906)
- **Original**: निरन्तर बहुत-सी दक्षिणाओंवाले यज्ञ करता रहता है, उससे ऋषि और पितरोंका भरण-पोषण कैसे किया जा सकता है ?
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5906)
- **Original**: निरन्तर बहुत-सी दक्षिणाओंवाले यज्ञ करता रहता है, उससे ऋषि और पितरोंका भरण-पोषण कैसे किया जा सकता है ?
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5907)
- **Original**: बढ़कर धर्मपरायण कौन होगा ?” मैं तो समझती हूँ आपका यह सारा परिश्रम व्यर्थ है। आपने “(इस तरह रानीके समझानेसे जनकने संनन्‍्यासका कमोंकों त्यागा है; इसलिये देखता, अतिथि और पितरोंने
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5907)
- **Original**: बढ़कर धर्मपरायण कौन होगा ?” मैं तो समझती हूँ आपका यह सारा परिश्रम व्यर्थ है। आपने “(इस तरह रानीके समझानेसे जनकने संनन्‍्यासका कमोंकों त्यागा है; इसलिये देखता, अतिथि और पितरोंने
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5908)
- **Original**: विचार छोड़ दिया।) राजा जनक संसारमें तस्ववेत्ताके रूपमें आपका भी परित्याग कर दिया है। आपके रहते ही आपकी
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5908)
- **Original**: विचार छोड़ दिया।) राजा जनक संसारमें तस्ववेत्ताके रूपमें आपका भी परित्याग कर दिया है। आपके रहते ही आपकी
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5909)
- **Original**: प्रसिद्ध हैं, किंतु उन्हें भी मोह हो गया था। उन्हींकी भाँति माता आजसे पुत्रहीना हुई और यह अभागिनी कौसल्या भी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5909)
- **Original**: प्रसिद्ध हैं, किंतु उन्हें भी मोह हो गया था। उन्हींकी भाँति माता आजसे पुत्रहीना हुई और यह अभागिनी कौसल्या भी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5910)
- **Original**: आप भी मोहमें न पड़िये । यदि हपलोग सर्वदा दान और तपें पतिहीना। भल्ला, कहिये तो--ये नाना प्रकारके बस्ध तथा
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5910)
- **Original**: आप भी मोहमें न पड़िये । यदि हपलोग सर्वदा दान और तपें पतिहीना। भल्ला, कहिये तो--ये नाना प्रकारके बस्ध तथा
- **Translation**: 

---

