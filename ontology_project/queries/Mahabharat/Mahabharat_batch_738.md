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

### Verse 1 (Mahabharat 0.7371)
- **Original**: ब्राह्मणोंकी पूजा, देवताओंको नमस्कार और गुरुजनोंको प्रणाम बुद्धिमान्‌ वस्के साथ उसका ब्याह कर दे । पुत्रका विवाह भी उत्तम
- **Translation**: 

---

### Verse 2 (Mahabharat 0.7371)
- **Original**: ब्राह्मणोंकी पूजा, देवताओंको नमस्कार और गुरुजनोंको प्रणाम बुद्धिमान्‌ वस्के साथ उसका ब्याह कर दे । पुत्रका विवाह भी उत्तम
- **Translation**: 

---

### Verse 3 (Mahabharat 0.7372)
- **Original**: खानके बाद ही करने चाहिये । बिना बुल्म्ये कहीं भी जाना उचित कुलकी कत्याके साथ करे और भृत्य भी अच्छे कुलके मनुष्योंको
- **Translation**: 

---

### Verse 4 (Mahabharat 0.7372)
- **Original**: खानके बाद ही करने चाहिये । बिना बुल्म्ये कहीं भी जाना उचित कुलकी कत्याके साथ करे और भृत्य भी अच्छे कुलके मनुष्योंको
- **Translation**: 

---

### Verse 5 (Mahabharat 0.7373)
- **Original**: नहीं है; किंतु यज्ञ देखनेके लिये बिना निमजणके भी जानेमें कोई ही बनावे। मस्तकपरसे खान करके देवकार्य तथा पितृकार्य करे।
- **Translation**: 

---

### Verse 6 (Mahabharat 0.7373)
- **Original**: नहीं है; किंतु यज्ञ देखनेके लिये बिना निमजणके भी जानेमें कोई ही बनावे। मस्तकपरसे खान करके देवकार्य तथा पितृकार्य करे।
- **Translation**: 

---

### Verse 7 (Mahabharat 0.7374)
- **Original**: हर्ज नहीं है। जहाँ अपना आदर न होता हो वहाँ जानेसे आयुका जिस नक्षत्रमें अपना जन्म हुआ हो उसमें श्राद्ध करना वर्जित है।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.7374)
- **Original**: हर्ज नहीं है। जहाँ अपना आदर न होता हो वहाँ जानेसे आयुका जिस नक्षत्रमें अपना जन्म हुआ हो उसमें श्राद्ध करना वर्जित है।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.7375)
- **Original**: ना होता है। अकेले परदेश जाना और रातमें यात्रा करना मना पूर्वा और उत्तराभाद्रपदा तथा कृत्तिका नक्षत्रमें भी श्राद्धका निषेध
- **Translation**: 

---

### Verse 10 (Mahabharat 0.7375)
- **Original**: ना होता है। अकेले परदेश जाना और रातमें यात्रा करना मना पूर्वा और उत्तराभाद्रपदा तथा कृत्तिका नक्षत्रमें भी श्राद्धका निषेध
- **Translation**: 

---

### Verse 11 (Mahabharat 0.7376)
- **Original**: है। यदि किसी कामके लिये बाहर जाय तो संध्या होनेके पहले हो है। (आइलेया, आदर, ज्येझ्ा और मूछ आदि) सम्पूर्ण दारुण
- **Translation**: 

---

### Verse 12 (Mahabharat 0.7376)
- **Original**: है। यदि किसी कामके लिये बाहर जाय तो संध्या होनेके पहले हो है। (आइलेया, आदर, ज्येझ्ा और मूछ आदि) सम्पूर्ण दारुण
- **Translation**: 

---

### Verse 13 (Mahabharat 0.7377)
- **Original**: घर ल्लौट आना चाहिये। माता- पिता और गुरुजनोंकी आज्ञाका नक्षत्रों और प्रत्यरि' तारका भी परित्याग कर देना चाहिये।
- **Translation**: 

---

### Verse 14 (Mahabharat 0.7377)
- **Original**: घर ल्लौट आना चाहिये। माता- पिता और गुरुजनोंकी आज्ञाका नक्षत्रों और प्रत्यरि' तारका भी परित्याग कर देना चाहिये।
- **Translation**: 

---

### Verse 15 (Mahabharat 0.7378)
- **Original**: अविलम्ब पालन करना चाहिये। उनकी आज्ञा हितकर है यां सारांश यह कि ज्यौतिष झाल्रके भीतर जिन-जिन नक्षत्रों
- **Translation**: 

---

### Verse 16 (Mahabharat 0.7378)
- **Original**: अविलम्ब पालन करना चाहिये। उनकी आज्ञा हितकर है यां सारांश यह कि ज्यौतिष झाल्रके भीतर जिन-जिन नक्षत्रों
- **Translation**: 

---

### Verse 17 (Mahabharat 0.7379)
- **Original**: अहितकर, इसका बिचार नहीं करना चाहिये। श्राद्धका निषेध किया गया है, उन सबसें देवकार्य और पितृकार्य
- **Translation**: 

---

### Verse 18 (Mahabharat 0.7379)
- **Original**: अहितकर, इसका बिचार नहीं करना चाहिये। श्राद्धका निषेध किया गया है, उन सबसें देवकार्य और पितृकार्य
- **Translation**: 

---

### Verse 19 (Mahabharat 0.7380)
- **Original**: युधिष्ठिर ! क्षत्रियको वेद और धयुवेंदके अभ्यासका यत्र नहीं करना चाहिये। पूर्व या उत्तकी ओर मुँह करके हजामत
- **Translation**: 

---

### Verse 20 (Mahabharat 0.7380)
- **Original**: युधिष्ठिर ! क्षत्रियको वेद और धयुवेंदके अभ्यासका यत्र नहीं करना चाहिये। पूर्व या उत्तकी ओर मुँह करके हजामत
- **Translation**: 

---

