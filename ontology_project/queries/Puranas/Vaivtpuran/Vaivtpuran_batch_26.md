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

### Verse 1 (Vaivtpuran 3.18335)
- **Original**: अन्दे चानन्दपूर्व त॑ परमात्मानमी श्वरम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.18336)
- **Original**: य॑ च॒ स्तोतुमशक्ताश्व ब्रह्मविष्णुशिवादय: । बेदा अहँ च वाणी च बच्दे त॑ं प्रकृते: परम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.18337)
- **Original**: बेदाश्न विदुषां भ्रेष्ठा: स्तोतुं शक्ता न लक्षतः । निर्लक्ष्य कः क्षमः स्तोतु त॑ निरीहं नमाम्यहम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.18338)
- **Original**: इत्येबमुक्त्वा दुर्गा रत्नसिंहासने खरे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.18339)
- **Original**: उयास नत्वा श्रीकृष्ण तुष्ठुघुस्तां सुरेश्वरा:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.18340)
- **Original**: डति दुर्गाकृतं स्तोच्नं कृष्णस्य परमात्मन: । यः पठेदर्चनाकाले स जयी सर्वतः सुखी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.18341)
- **Original**: दुर्गा तस्य गृहं त्यक्त्वा नैव याति कदाचन । भवाव्धौं यशसा भाति यात्वन्ते श्रीहरे: पुरम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.18342)
- **Original**: उति अरीब्रह्मवैवर्ते दुर्गाकृतं श्रीकृष्णस्तोत्र सम्पूर्णय्‌। ( ब्रह्मखण्ड 3
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.18343)
- **Original**: 77--87 ) #नाजल्‍> एल एल00 /90क्‍5000
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8425)
- **Original**: 392 + संक्षिप्त ग्रह्मवैवर्तपुराण * परशुरामको गौरीका स्तवन करनेके लिये कहकर विष्णुका बैकुण्ठ-गमन, परशुरामका पार्वतीकी स्तुति करना .. कहते हैं-- नारद! इस प्रकार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8426)
- **Original**: था, उस भयंकर समयमें ये सती सम्पूर्ण पार्वतीको समझा-बुझाकर भगवान्‌ विष्णु परशुरामसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8427)
- **Original**: देवताओंके तेजसे आविर्भूत हुई थीं। तत्पश्चात्‌ हितकारक, तत्त्वस्वरूप, नीतिका साररूप और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8428)
- **Original**: श्रीकृष्णकी आज्ञासे इन्होंने असुरोंका वध करके परिणाममें सुखदायक वचन बोले। देवताओंका पद उन्हें प्रदान किया। फिर दक्षकौ विष्णुने कहा--राम! तुमने अकल्याणकर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8429)
- **Original**: तपस्याके कारण दक्षपत्रीके गर्भसे जन्म लिया। मार्गपर स्थित हो क्रोधवश जो गणेशका दाँत तोड़
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8430)
- **Original**: उस जन्ममें सती शंकरकी भार्या हुईं। पुनः पतिकी डाला है, इससे तुम श्रुतिके मतानुसार इस समय
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8431)
- **Original**: निन्दाके कारण उस शरीरको त्यागकर इन्होंने सचमुच ही अपराधी हो। अतएव मेरेद्वारा शैलराजकी पत्नीके गर्भसे जन्म धारण किया। फिर बतलाये हुए स्तोत्रसे देवश्रेष्ठ गणपतिका स्तवन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8432)
- **Original**: तपस्या करके योगीन्द्रोंके गुरुके गुरु शंकरको करके पुनः काण्वशाखामें कहे हुए स्तोत्रद्वारा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8433)
- **Original**: पाया और श्रोकृष्णकी सेवासे श्रीकृष्णके अंशभूत जगज्जननी दुर्गाकी स्तुति करो। ये जगदीश्वर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8434)
- **Original**: गणपतिको पुत्ररूपमें प्राप्त किया। बालक! जिनका श्रीकृष्णकी परा शक्ति एवं बुद्धिस्वरूपा हैं। इनके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8435)
- **Original**: तुम नित्य ध्यान करते हो, क्या उन्हें नहीं जानते ? रुष्ट हो जानेपर तुम्हारी बुद्धि नष्ट हो जायगी।
- **Translation**: 

---

