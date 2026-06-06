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

### Verse 1 (Vaivtpuran 4.8596)
- **Original**: किस हेतुसे और कहाँ उनका आविर्भाव हुआ? भगवान्‌ नारायण, नरश्रेष्ठ नर तथा देवी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8597)
- **Original**: उनके पिता वसुदेव कौन थे अथवा माता देवकी सरस्वतीकों नमस्कार करके जय (इतिहास-पुराण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8598)
- **Original**: भी कौन थीं? बताइये। किसके कुलमें भगवानने आदि)-का पाठ करना चाहिये। मायाद्वारा जन्म-ग्रहणकी लीला की? श्रीहरिने नारदजीने कहा--ब्रह्मन्‌! मैंने सबसे पहले
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8599)
- **Original**: किस रूपसे यहाँ आकर क्या किया? मुने! सुना पूज्यपाद पिता ब्रह्माजीके मुखारविन्दसे ब्रह्मखण्डकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8600)
- **Original**: जाता है कि श्रीकृष्ण कंसके भयसे सूतिकागृहसे मनोहर कथा सुनी है, जो अत्यन्त अद्भुत है।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8601)
- **Original**: गोकुलको चले गये थे। जो स्वयं भयके स्वामी तदनन्तर उन्हींकी आज्ञासे मैं तुरंत आपके निकट
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8602)
- **Original**: हैं, उन्हें कौटतुल्य कंससे क्‍यों भय हुआ? उन चला आया और यहाँ अमृतखण्डसे भी अधिक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8603)
- **Original**: श्रीहरिने गोप-वेष धारण करके गोकुलमें कौन- मधुर प्रकृतिखण्ड सुननेको मिला। तत्पश्चात्‌ मैंने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8604)
- **Original**: सी लीला की? बे तो जगदीश्वर हैं। फिर उन्होंने गणपतिखण्ड श्रवण किया, जो अखण्ड जन्मोंका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8605)
- **Original**: गोपाड्नाओंके साथ क्‍यों विहार किया? गोपाब्ननाएँ खण्डन करनेवाला है। परंतु मेश लोलुप मन अभी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8606)
- **Original**: कौन थीं? अथवा वे ग्वाल-बाल भी कौन थे? तृप्त नहीं हुआ। यह और भी विशिष्ट प्रसड्ञको
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8607)
- **Original**: यशोदा कौन थीं? नन्दरायजी कौन थे? उन्होंने सुनना चाहता है। अत: अब श्रीकृष्णजन्मखण्डका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8608)
- **Original**: कौन-सा पुण्य किया था? श्रीहरिकी प्रेयसी विस्तारपूर्वक वर्णन कीजिये, जो मनुष्योंके जन्म-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8609)
- **Original**: गोलोकवासिनी पुण्यवती देवी श्रीराधा क्यों ब्रजमें मरण आदिका खण्डन करनेवाला है। बह समस्त
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8610)
- **Original**: ब्रजकन्या होकर प्रकट हुईं? गोपियोंने किस तत्त्वोंका प्रकाशक, कर्मबन्धनका नाशक, हरिभक्ति
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8611)
- **Original**: प्रकार दुरारध्य परमेश्वरकों प्राप्त किया? श्रीहरि प्रदान करनेवाला, तत्काल वैराग्यजनक, संसारविषयक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8612)
- **Original**: उन सबको छोड़कर मथुरा क्‍यों चले गये? आसक्तिका निवारक, मुक्तिबीजका कारण तथा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8613)
- **Original**: महाभाग! पृथ्वीका भार उतारकर कौन-सी लीला भवसागरसे पार उतारनेवाला उत्तम साधन है। वह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8614)
- **Original**: करनेके पश्चात्‌ भगवान्‌ श्रीकृष्ण पुन: परमधामको कर्मभोगरूपी रोगोंका नाश करनेके लिये रसायनका काम देता है। श्रीकृष्णचरणारविन्दोंकी प्राप्तिके लिये सोपानका निर्माण करता है। वैष्णवोंका तो वह जीवन ही है। तीनों लोकोंको परम पवित्र करनेवाला है। मैं आपका शरणागत भक्त एवं शिष्य हूँ। अत: आप मुझे श्रीकृष्णजन्मखण्डकी कथाको विस्तारपूर्वक सुनाइये। किसकी प्रार्थनासे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8615)
- **Original**: पुरुषोंक करोड़ों जन्मोंकी पापराशिका यह नाश एकमात्र परिपूर्णतम परमेश्वर श्रीकृष्ण अपने सम्पूर्ण
- **Translation**: 

---

