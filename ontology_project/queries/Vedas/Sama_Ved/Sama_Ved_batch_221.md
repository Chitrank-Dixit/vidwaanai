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

### Verse 1 (Sama Ved 0.4401)
- **Original**: 19728. एपो उषा अपूर्व्या व्युच्छति प्रिया दिवः । स्तुषे वामश्विना बृहत्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4402)
- **Original**: यह प्रिय अपूर्व उषा आकाश के तम का नाश करती है । हे अश्विनीकुमारों । हम महान्‌ स्तोत्रों द्वारा आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4403)
- **Original**: 1729. या दस्रा सिन्धुमातरा मनोतरा रयीणाम्‌ । धिया देवा वसुविदा
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4404)
- **Original**: ये अश्विनीकुमार शत्रुओं के नाशक, नदियों के उत्पत्तिकर्ता, विवेकपूर्वक कर्म करने वालों को सम्पत्ति देने वाले हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4405)
- **Original**: 1730, वच्यन्ते वां ककुहासो जूर्णायामधि विष्टपि। यद्वां रथो विभिष्पतात्‌। ।6
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4406)
- **Original**: है अश्विनीकुमारों । जब आपका रथ पक्षियों की तरह आकाश में पहुँचता है, तब प्रशंसनीय स्वर्ग लोक में भी आपके लिए स्तोत्रों का पाठ किया जाता है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4407)
- **Original**: 1731. उषस्तच्चित्रमा भरास्मभ्यं वाजिनीवति । येन तोक॑ च तनय॑ च धामहे ।।7
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4408)
- **Original**: हे हवनों को प्रारम्भ करने वाली उषे ! हमें वह विलक्षण ऐश्वर्य प्रदान करें, जिससे हम सन्तानादि का पोषण कर सकें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4409)
- **Original**: 1732. उषो अद्येह गोमत्यश्वावति विभावरि । रेवदस्मे व्युच्छ सूनृतावति
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4410)
- **Original**: गौओं और अश्वों से युक्त, यज्ञ कर्मों की प्रेरक हे उपे ! आप आज हमें धन-धान्य से युक्त करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4411)
- **Original**: 1733. युंक्षा हि वाजिनीवत्यश्वाँ अद्यारुणाँ उषः । अथा नो विश्वा सौभगान्या वह
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4412)
- **Original**: ही हे हवनों को प्रारम्भ कराने वाली उबे ! आप अरुणाभ अश्वों (किरणों) को अपने रथ से युक्त करें और हमें विश्व के सब सौभाग्य प्रदान करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4413)
- **Original**: 1734. अश्निना वर्तिरस्मदा गोमदज्ला हिरण्यवत्‌ । अर्वाग्रथ॑ समनसा नि यच्छतम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4414)
- **Original**: है अश्विनीकुमारों ! शत्रुगुशक आप, गौओं और स्वर्णमय रथ को मनोयोगपूर्वक हम्मारी ओर प्रेरित करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4415)
- **Original**: 1735. एह देवा मयोभुवा दस््रा हिरण्यवर्तनी । उषर्बुधो वहन्तु सोमपीतये
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4416)
- **Original**: उषा के साथ जाग्रत किरणें (अश्व) स्वर्णिम प्रकाश में स्थित दुःखनिवारक एवं सुखदायी अश्विनीकुमारों को इस यज्ञ में सोमपान के लिए लाएँ
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4417)
- **Original**: 19.ड सामवेद-संहिता 1736. यावित्था श्लेकमा दिवो ज्योतिर्जनाय चक्रथु: । आन ऊर्ज वहतमश्विना युवम्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4418)
- **Original**: है अश्विनीकुमारो ! आप द्युलोक से प्रशंसा योग्य प्रकाश लाकर लोगों का हित करते हैं, ऐसे आप हमें अन से पुष्ट करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4419)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4420)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

