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

### Verse 1 (Vaivtpuran 56.5372)
- **Original**: उस महादेवीके द्वारा पूजित देवताका नाम महादेव सदा 'शं' अर्थात्‌ कल्याण करते हैं, वे ही शंकर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 56.5373)
- **Original**: है। विश्वमें स्थित जितने महान्‌ हैं, उन सबके वे कहे गये हैं। कल्याणका तात्पर्य यहाँ मोक्षसे है।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 56.5374)
- **Original**: ईश्वर हैं। इसलिये मनीषी पुरुष इन्हें महेश्वर कहते ब्राद्मा आदि देवता तथा बेदबादी मुनि-ये महान्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 56.5375)
- **Original**: हैं।* ब्रह्मपुत्र नारद! तुम धन्य हो, जिसके गुरु कहे गये हैं। उन महान्‌ पुरुषोंके जो देवता हैं,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 56.5376)
- **Original**: श्रीकृष्णभक्ति प्रदान करनेवाले साक्षात्‌ महे श्वर हैं। उन्हें महादेव कहते हैं। सम्पूर्ण विश्वरमें पूजित
- **Translation**: 

---

### Verse 6 (Vaivtpuran 56.5377)
- **Original**: फिर तुम मुझसे क्यों पूछ रहे हो! (अध्याय 56) #8897/8 5 फसफक95..>>>ज दुर्गाजीके सोलह नामोंकी व्याख्या, दुर्गाकी उत्पत्ति तथा उनके पूजनकी परम्पराका संक्षिप्त वर्णन नारदजी बोले--ब्रह्मन्‌! मैंने अत्यन्त अद्भुत
- **Translation**: 

---

### Verse 7 (Vaivtpuran 56.5378)
- **Original**: शब्द दैत्य, महाविप्र, भवबन्धन, कर्म, शोक, सम्पूर्ण उपाख्यानोंकों सुना। अब दुर्गाजीके उत्तम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 56.5379)
- **Original**: दुःख, नरक, यमदण्ड, जन्म, महान्‌ भय तथा उपाख्यानको सुनना चाहता हूँ। वेदकी कौथुमी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 56.5380)
- **Original**: अत्यन्त रोगके अर्थमें आता है तथा 'आ' शब्द शाखामें जो दुर्गा, नारायणी, ईशाना, विष्णुमाया,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 56.5381)
- **Original**: 'हन्ता' का वाचक है। जो देवी इन दैत्य और शिवा, सती, नित्या, सत्या, भगवती, सर्वाणी,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 56.5382)
- **Original**: महाविघश्न आदिका हनन करती है, उसे “दुर्गा सर्वमड्जला, अम्बिका, वैष्णवी, गौरी, पार्वती और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 56.5383)
- **Original**: कहा गया है। यह दुर्गा यश, तेज, रूप और सनातनी--ये सोलह नाम बताये गये हैं, वे सबके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 56.5384)
- **Original**: गुणोंमें नारायणके समान है तथा नारावणकी ही लिये कल्याणदायक हैं। वेदवेत्ताओंमें श्रेष्ट नारायण !
- **Translation**: 

---

### Verse 14 (Vaivtpuran 56.5385)
- **Original**: शक्ति है। इसलिये “नारायणी' कही गयी है। इन सोलह नामोंका जो उत्तम अर्थ है, वह सबको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 56.5386)
- **Original**: ईशानाका पदच्छेद इस प्रकार है->ईशान+आ। अभीष्ट है। उसमें सर्बसम्मत वेदोक्त अर्थजो आप
- **Translation**: 

---

### Verse 16 (Vaivtpuran 56.5387)
- **Original**: 'ईशान' शब्द सम्पूर्ण सिद्धियोंके अर्थमें प्रयुक्त बताइये। पहले किसने दुर्गाजीकी पूजा कौ है?
- **Translation**: 

---

### Verse 17 (Vaivtpuran 56.5388)
- **Original**: होता है और 'आ' शब्द दाताका बाचक है। जो फिर दूसरी; तीसरी और चौथी बार किन-किन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 56.5389)
- **Original**: सम्पूर्ण सिद्धियोंकों देनेवाली है, वह देवी 'ईशाना' लोगोंने उनका सर्वत्र पूजन किया है? कही गयी है। पूर्वकालमें सृष्टिके समय परमात्मा श्रीनारायणने कहा--देवर्षे ! भगवान्‌ विष्णुने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 56.5390)
- **Original**: विष्णुने मायाकी सृष्टि कौ थी और अपनी उस वेदमें इन सोलह नामोंका अर्थ किया है, तुम उसे । मायाद्वारा सम्पूर्ण विश्वकों मोहित किया। बह जानते हो तो भी मुझसे पुनः पूछते हो। अच्छा,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 56.5391)
- **Original**: मायादेवी विष्णुकी ही शक्ति हैं, इसलिये 'विष्णुमाया' मैं आगमोंके अनुसार उन नामोंका अर्थ कहता हूँ। कही गयी है। 'शिवा' शब्दका पदच्छेद यों दुर्गा शब्दका पदच्छेद यों है-दुर्गगआ। दुर्ग!
- **Translation**: 

---

