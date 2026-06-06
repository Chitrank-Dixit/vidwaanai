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

### Verse 1 (Bramha 0.6381)
- **Original**: शत्रुओंका दर्प दलन करनेमें समर्थ हैं। अरी सखी ! अरिष्ट, धेनुक तथा केशी आदि दुराचारियोंकों
- **Translation**: 

---

### Verse 2 (Bramha 0.6382)
- **Original**: उधर देखो, मुष्टिक और चाणूरको उछलते-कूदते खेल-खेलमें ही मार डाला, वे ही ये श्रीकृष्ण
- **Translation**: 

---

### Verse 3 (Bramha 0.6383)
- **Original**: देख बलभद्रजीके मुखपर मन्द हास्यकी कैसी छटा दिखायी देते हैं और ये जो दूसरे महाबाहु
- **Translation**: 

---

### Verse 4 (Bramha 0.6384)
- **Original**: छा रही है। हाय, सखी! देखो तो सहो, ये श्रोकृष्ण युवतियोंके मन और नयनोंको आनन्द देते हुए
- **Translation**: 

---

### Verse 5 (Bramha 0.6385)
- **Original**: चाणूरके साथ युद्ध करने जा रहे हैं। क्या इस सभामें लीलापूर्वक आगे- आगे चल रहे हैं, वे श्रीकृष्णके
- **Translation**: 

---

### Verse 6 (Bramha 0.6386)
- **Original**: न्याययुक्त बर्ताव करनेवाले बड़े-बूढ़े नहीं हैं? कहाँ बड़े भाई बलदेवजों हैं। पौराणिक रहस्यको तो अभी युवावस्थामें प्रवेश करनेवाले श्रीहरिका जाननेवाले विद्वान्‌ पुरुष इन्हीं गोपालके विषयमें सुकुमार शरोर और कहाँ बज़के समान कठोर एबं यों कहते हैं कि ये शोकसागरमें डूबे हुए विशाल शरीरबाला यह महान्‌ असुर! ये दोनों भाई
- **Translation**: 

---

### Verse 7 (Bramha 0.6387)
- **Original**: » कुब्णापर कृपा, कुकलवापीड, चाणूर, मुष्टिक, तोशल और कंस आदिका वध * 307 रड्रभूमिमें अभी तरुण दिखायी देते हैं। इनके
- **Translation**: 

---

### Verse 8 (Bramha 0.6388)
- **Original**: डालिये, गोविन्द! आपकी जय हो।' सभी अड्ग कोमल हैं और चाणूर आदि दैत्य मल्ल
- **Translation**: 

---

### Verse 9 (Bramha 0.6389)
- **Original**: श्रीकृष्ण देस्तक चाणूरके साथ खिलवाड़ बड़े ही भयंकर हैं। युद्धेके लिये जोड़का चुनाव
- **Translation**: 

---

### Verse 10 (Bramha 0.6390)
- **Original**: करते रहे, फिर उसे मार डालनेके लिये सरचेष्ट हुए करनेवाले लोगोंका यह यहुत बड़ा अन्याय है कि
- **Translation**: 

---

### Verse 11 (Bramha 0.6391)
- **Original**: और दैत्यको उठाकर आकाशमें घुमाने लगे। ये मध्यस्थ होकर भी बालक और बलवानूके
- **Translation**: 

---

### Verse 12 (Bramha 0.6392)
- **Original**: घुमाते समय हो उसके प्राण-पखेरू उड़ गये। युद्धकी उपेक्षा करते हैं।' भगवानने उसे सौ बार घुमाकर पृथ्वीपर पटक जब नगरकी स्त्रियाँ इस प्रकार वार्तालाप कर
- **Translation**: 

---

### Verse 13 (Bramha 0.6393)
- **Original**: दिया। चाणूरके सौ-सौ टुकड़े हो गये। उसके रही थीं, उसी समय भगवान्‌ श्रोहरि अपने
- **Translation**: 

---

### Verse 14 (Bramha 0.6394)
- **Original**: रक्तकी धारासे अखाड़ेमें गहरी कौचड़ हो गयी। पदाघातसे पृथ्वीको कैंपाते हुए सब लोगोंके
- **Translation**: 

---

### Verse 15 (Bramha 0.6395)
- **Original**: महाबली बलदेवजी भी उतनी देरतक मुष्टिकके हुृदयमें हर्षातिरिककी वृष्टि करने लगे। बलभद्रजी
- **Translation**: 

---

### Verse 16 (Bramha 0.6396)
- **Original**: साथ लड़ते रहे। अन्तमें उन्होंने भी उस दैत्यके भी ताल ठोंककर मनोहर गतिसे उछलते हुए चल
- **Translation**: 

---

### Verse 17 (Bramha 0.6397)
- **Original**: मस्तकपर मुकेका प्रहार किया और छातीमें रहे थे। उस समय यह पृथ्वी पग-पगपर उनके
- **Translation**: 

---

### Verse 18 (Bramha 0.6398)
- **Original**: घुटनेसे आघात करके उसे पृथ्वीपर गिरा दिया। पदाघातसे विदीर्ण नहीं हुई-यही बड़े आश्चर्यकी
- **Translation**: 

---

### Verse 19 (Bramha 0.6399)
- **Original**: फिर अपने शरीरसे रगड़कर उसका कचूमर बात थी। तदनन्तर अमितपराक्रमी श्रीकृष्ण चाणूरके
- **Translation**: 

---

### Verse 20 (Bramha 0.6400)
- **Original**: निकाल दिया। उसकी जीवन-लौला समाप्त हो साथ कुश्ती लड़ने लगे तथा मल्नयुद्धकी विद्यामें
- **Translation**: 

---

