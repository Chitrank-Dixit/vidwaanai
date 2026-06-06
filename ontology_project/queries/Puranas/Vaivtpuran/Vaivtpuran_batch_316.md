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

### Verse 1 (Vaivtpuran 15.6673)
- **Original**: देखकर कृत्तिकाओंका हृदय दुःखसे फटा जा रहा जनक और मोह-जालके उच्छेदक हैं तथा ब्रह्मा,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6674)
- **Original**: था। उनके केश खुल गये थे और वे शोकसे विष्णु और शिव आदि सभी देवगण जिनका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6675)
- **Original**: व्याकुल थीं। सहसा चेतना प्राप्त होनेपर अपने निरन्तर भजन करते हैं, उन गोविन्दकौ भक्ति [सामने स्कन्दकों देख वे अत्यन्त शोकके कारण कीजिये। इस भवसागरमें मैं आपलोगोंका कौन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6676)
- **Original**: ठगी-सी रह गयीं; फिर वहीं भयवश उन्मत्तकी हूँ और आपलोग मेरी कौन हैं? संसार-प्रवाहका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6677)
- **Original**: भाँति कहने लगीं। वह सारा कर्म फेनकी भाँति पुझीभूत हो गया
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6678)
- **Original**: । . कृत्तिकाओंने कहा--हाय! अब हमलोग है। (वस्तुतः कोई किसीका नहीं है।) संयोग
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6679)
- **Original**: क्या करें, कहाँ चली जाये? बेटा! हमारे आश्रय अथवा वियोग--यह सब ईश्वरकी इच्छासे ही
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6680)
- **Original**: तो तुम्हीं हो। इस समय तुम हमलोगोंको छोड़कर . होता है। यहाँतक कि सारा ब्रह्माण्ड ईश्वरके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6681)
- **Original**: कहाँ जा रहे हो? यह तुम्हारे लिये धर्मसड्भत बात अधीन है, वह भी स्वतन्त्र नहीं है-ऐसा विद्वान्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6682)
- **Original**: नहीं है। हमलोगोंने बड़े स्नरेहसे तुम्हें पाला-पोसा लोग कहते हैं। सारी त्रिलोकी जलके बुलबुलेके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6683)
- **Original**: है, अत: तुम धर्मानुसार हमारे पुत्र हो। भला, समान क्षणभद्भुर है, फिर भी मायासे मोहित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6684)
- **Original**: उपयुक्त पुत्र मातृवर्गोंका परित्याग कर दे--यह भी चित्तवाले लोग इस अनित्य जगतूमें मायाका कोई धर्म है? यों कहकर सभी कृत्तिकाओंने विस्तार करते हैं; परंतु जो श्रीकृष्णपरायण संत
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6685)
- **Original**: कार्तिकेयकों छातीसे चिपका लिया और पुत्र- हैं, वे जगत्‌में रहते हुए भी वायुकी भाँति लिप्त
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6686)
- **Original**: वियोगजन्य दारुण दुःखके कारण वे पुन: मूर्च्छित नहीं होते। इसलिये माताओ! आपलोग मोहका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6687)
- **Original**: हो गयीं। मुने! तत्पश्चात्‌ कुमार कार्तिकेयने परित्याग करके मुझे जानेकी आज्ञा दीजिये। [आध्यात्मिक वचनोंद्वारा उन्हें समझाया और फिर यों कहकर ऐश्वर्यशाली कार्तिकेयने उन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6688)
- **Original**: उनके तथा पार्षदोँंके साथ वे उस रथपर सवार कृत्तिकाऑंको नमस्कार किया और फिर मन-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6689)
- **Original**: हुए। मुने ! यात्राकालमें उन्होंने अपने सामने साँड, ही-मन श्रीहरिका स्मरण करते हुए शंकरजीके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6690)
- **Original**: गजराज, घोड़ा, जलती हुई आग, भरा हुआ पार्षदोंके साथ यात्राके लिये प्रस्थान किया। इसी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6691)
- **Original**: सुवर्ण-कलश, अनेक प्रकारके पके हुए फल, बीच उन्होंने वहाँ एक उत्तम रथकों देखा। वह
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6692)
- **Original**: पति-पुत्रसे युक्त स्त्री, प्रदीप, उत्तम मणि, मोती, बहुमूल्य रत्रोंका बना हुआ था, जिसे विश्वकर्माने
- **Translation**: 

---

