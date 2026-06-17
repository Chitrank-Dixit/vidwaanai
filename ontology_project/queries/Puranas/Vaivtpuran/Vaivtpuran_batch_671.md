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

### Verse 1 (Vaivtpuran 67.18904)
- **Original**: त्वया शोभा यशोदाया नन्दस्थ नन्दनन्दन
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.18905)
- **Original**: यथा शाखाफलस्कन्थैस्तरुराजिर्विराजते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.18906)
- **Original**: त्वया सार्ध गोकुलेश शोभा गोकुलवासिनाम्‌ । यथा सर्वा लोकराजी राजेन्द्रेण विराजते
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.18907)
- **Original**: रासस्थापि च रासेश त्वया शोभा मनोहरा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.18908)
- **Original**: राजते देवराजेन यथा स्वर्गेईमरावती
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.18909)
- **Original**: वृन्दावनस्थ वृक्षाणां त्व॑ च शोभा पतिर्गति:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.18910)
- **Original**: अन्येषां च बनानां च बलवान्‌ केसरी यथा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.18911)
- **Original**: त्वया बिना यशोदा अ्ञ निमग्रा शोकसागरे । अप्राप्य वत्सं सुरभि: क्रोशन्ती व्याकुला यथा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.18912)
- **Original**: आन्दोलयन्ति नन्दस्य प्राणा दग्धं च मानसम्‌। त्ववा विना तप्तपात्रे यथा धान्यसमूहक:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.18913)
- **Original**: इति औब्रह्मवैवर्ते रधाकृतं श्रीकृष्णस्तवन सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 67। 7-- 24) बअरह्यकृतं श्रीकृष्णस्तोत्रम्‌ ब्रह्मोवाच जय जय जगदीश बन्दितचरण निर्गुण निराकार स्वेच्छामय भक्तानुग्रहनित्यत्रिग्रह गोपवेष मायया मायेश सुवेष सुशील शान्‍्त सर्वकान्त दान्त नितान्तज्ञानानन्द परात्परतर प्रकृतेः पर सर्वान्तरात्मरूप निर्लिप्त साक्षिस्वरूप व्यक्ताव्यक्त निरश्षन भारावतारण करुणार्णव शोकसंतापग्रसन जरामृत्युभयादिहरण शरणपञ्ञर भक्तानुग्रहकातर भक्तवत्सल भक्तसंचितधन 34 नमोस्तु ते
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.18914)
- **Original**: सर्वाधिष्ठातृदेबायेत्युक्ला ले प्रीणनाय च् । पुनः पुनरुबाचेदद मूर्च्छितक्ष बभूव ह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.18915)
- **Original**: इति ब्रह्मकृतं स्तोत्र यः थ्रूणोति समाहित: । तत्सवभीष्टसिद्धिश्ष भवत्येव न संशय:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.18916)
- **Original**: अपुत्रों लभते पुत्र॑ प्रियाहीनो लभेत्‌ प्रियाम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.18917)
- **Original**: निर्धनो लभते सत्य॑ परिपूर्णतमं धनम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.18918)
- **Original**: इह लोके सुखं भुक्त्या चान्ते दास्य॑ लभेद्धरेः। अचलां भक्तिमाप्नोति मुक्तेरपि सुदुर्लभाम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.18919)
- **Original**: ज्ति श्रीब्रह्मवैवतें ब्रह्मकृतं श्रीकृष्णस्तोजं सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 69। 23--27) हज पाए थ2502000 *
- **Translation**: 

---

### Verse 17 (Vaivtpuran 70.18920)
- **Original**: 826 + संक्षिप्त ब्रह्मवैवर्तपुराण « अक्रूरकृतं श्रीकृष्णस्तोत्रम्‌ अक्रूर उबाच नमः कारणरूपाय परमात्मस्वरूपिणे । सर्वेधामथि विश्वानामीश्वराय. नमो नमः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 70.18921)
- **Original**: पराय प्रकृतेश . परात्परतराथ. च । निर्गुणाय निरीहाय नीरूपाय स्वरूपिणे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 70.18922)
- **Original**: सर्वदेवस्वरूपाय सर्वदेवेश्वराय च । सर्वदेवाधिदेवाय विश्वादिभूतरूपिणे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 70.18923)
- **Original**: असंख्येषु च विश्वेषु ब्रह्मविष्णुशिवात्मक: । स्वरूपायादिबीजाय तदीशविश्वरूपिणे
- **Translation**: 

---

