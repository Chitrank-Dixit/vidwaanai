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

### Verse 1 (Rig Ved 0.10341)
- **Original**: [ सूक्त - 16 ] [ ऋषि - भरद्वाज बाईस्पत्य । देवता - अग्नि। छन्द - गायत्री; 1, 6वर्धमाना; 27, 47-48 अनुष्टपु: 46 ब्रिष्टप्‌। ] 4494. त्वमग्ने यज्ञानां होता विश्वेषां हित: । देवेभिमानुषे जने
- **Translation**: 

---

### Verse 2 (Rig Ved 0.10342)
- **Original**: है अग्निदेव ! आप होता और देवगणों के आवाहनकर्त्ता हैं । आप मनुष्यों के यज्ञ में देवताओं द्वारा होता निर्धारित किये गये हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.10343)
- **Original**: 20 ऋ्वेद संहिता घाग - 2 4495, स नो मन्द्राभिरध्वरे जिल्ाभिर्यजा मह:
- **Translation**: 

---

### Verse 4 (Rig Ved 0.10344)
- **Original**: आ देवान्वक्षि यक्षि च
- **Translation**: 

---

### Verse 5 (Rig Ved 0.10345)
- **Original**: है अग्निदिव ! आप अपनी महान्‌ ज्वालाओं सहित इस यज्ञ में देवगणों कौ स्तुति करें एवं इन्द्रादि देवताओं का आवाहन करके उन्हें हवि प्रदाव करें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.10346)
- **Original**: 4496. वेत्था हि वेधो अध्वन: पथश्च देवाउ्जसा । अग्ने यज्ञेषु सुक्रतो
- **Translation**: 

---

### Verse 7 (Rig Ved 0.10347)
- **Original**: है नियन्ता, श्रेष्ठकर्मा अग्निदेव ! आप यज्ञ के निकटस्थ एवं दूरस्थ (प्रत्यक्ष एवं अप्रत्यक्ष) सभी मार्गों के ज्ञाता हैं। आप याजकों का उचित मार्गदर्शन करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.10348)
- **Original**: 4497. त्वामीक्ठे अध द्विता भरतो वाजिभि: शुनम्‌। ईजे यज्ञेषु यज्ञियम्‌
- **Translation**: 

---

### Verse 9 (Rig Ved 0.10349)
- **Original**: हे तेजरूप अग्तिदेव ! भरत अनेक कत्विजों के साथ मिलकर लौकिक एवं अलौकिक दोनों प्रकार के सुख प्राप्त करमे के लिए आपकी स्तुति करते हैं। है यजनीय ! आपके द्वारा ही अनिष्टों का शमन एवं इच्छाओं की पूर्ति होती है । हम आपकी स्तुति और यज्ञ करते हैं
- **Translation**: 

---

### Verse 10 (Rig Ved 0.10350)
- **Original**: 4498. त्वमिमा वार्या पुरु दिवोदासाय सुन्वते। भरद्वाजाय दाशुषे
- **Translation**: 

---

### Verse 11 (Rig Ved 0.10351)
- **Original**: है अग्निदेव ! आपने सोम सिद्धकर्ता 'दिवोदास' को बहुत सा ऐश्वर्य प्रदान किया था; उसी प्रकार 'भरद्वाज' (हवि देने वाले को) भी धन-ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.10352)
- **Original**: 4499. त्वं दूतो अमर्त्य आ वहा दैव्यं जनम्‌
- **Translation**: 

---

### Verse 13 (Rig Ved 0.10353)
- **Original**: शृण्बन्िप्रस्य सुष्टुतिम्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.10354)
- **Original**: हे अग्निदेव ! आप अमर हैं, आप दूत हैं; ( अत)) विद्वान्‌ भरद्वाज द्वारा की जा रही स्तुति को सुनने के लिए देवगणों का हमारे यज्ञ में आवाहन करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.10355)
- **Original**: 4500. त्वामन स्वाध्यो3 मर्तासो देववीतये। यज्ञेषु देवमीव्ठते
- **Translation**: 

---

### Verse 16 (Rig Ved 0.10356)
- **Original**: बल अर्थात्‌ घर्षण से प्रकट होने वाले सौन्दर्यवान्‌ हे अग्निदेव ! हम याजकगण धन-धान्य एवं आपका सान्निध्य प्राप्त करने को कामना से वन्दना करते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.10357)
- **Original**: 4501. तब प्र यक्षि सन्दृशमुत क्रतुं सुदानवः । विश्वे जुघन्त कामिन:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.10358)
- **Original**: स्वर्ण सदृश जाज्वल्यमान है अग्निदेव ! ख्या में मिलने वालो शीतलता की तरह हम आपके संरक्षण में रहकर सुख प्राप्त करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.10359)
- **Original**: 4502, त्व॑ होता मनुर्हितो वह्िरासा विदुष्टर: । अग्ने यक्षि दिवो विश:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.10360)
- **Original**: बैल के सींग को भाँति तेजस्वी ज्वालाओं वाले, बोर धनुर्धर के समान पराक्रमी हे अग्निदेव ! आपने दुष्टो के आश्रय-स्थलों को नष्ट किया है
- **Translation**: 

---

